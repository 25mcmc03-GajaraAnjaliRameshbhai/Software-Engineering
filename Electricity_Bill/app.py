from flask import Flask,render_template,request, make_response
from database import get_connection
from datetime import datetime,timedelta
import pdfkit


app = Flask(__name__)
config = pdfkit.configuration(
  wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
)



def calculate_bill(units):
  if units <= 50:
    amount = units * 1.75
    
  elif units <=100:
    amount = (50 * 1.75) + ((units - 50) * 3)
  
  elif units <= 150:
    amount = (50 * 1.75) + (50 * 3) + ((units - 100) * 4.25)
    
  elif units <=200 :
    amount = (50 * 1.75) + (50 * 3) + (50 * 4.25) + ((units - 150) * 5.5)
  
  else :
    amount = (50 * 1.75) + (50 * 3) + (50 * 4.25) + (50 * 5.5) + ((units - 200) * 7.5)
  
  return amount 
     

@app.route('/')
def home():
  return render_template('index.html')


@app.route('/search', methods =['POST'])
def search() :
  
  consumer_no = request.form['consumer_no']
  conn = get_connection()
  cursor = conn.cursor(dictionary = True)
  query = """
  select * from consumers
  where consumer_no = %s"""
  cursor.execute(query,(consumer_no,))
  
  consumer = cursor.fetchone()
  return render_template('consumer.html',consumer=consumer)
  

@app.route('/generate_bill', methods=['POST'])
def generate_bill():
  consumer_no = request.form['consumer_no']
  units = int(request.form['units'])
  amount = calculate_bill(units)
  bill_no = f"BILL{consumer_no}{datetime.today().strftime('%Y%m%d%H%M%S')}"
  bill_date = datetime.today().date()
  due_date = bill_date + timedelta(days=15)
  
  
  conn = get_connection()
  cursor = conn.cursor(dictionary = True)
  
  cursor.execute("""
    select payable_amount from bills
    where consumer_no = %s
    order by bill_no desc limit 1""",
    (consumer_no,))
  
  last_bill =cursor.fetchone()
  
  if last_bill :
    previous_due = float(last_bill['payable_amount'])
  else :
    previous_due = 0.0
  current_bill = float(amount)
  payable_amount = previous_due + current_bill
  bill_month = datetime.today().strftime("%B")
  
  
  query ="""insert into bills(bill_no,consumer_no,bill_month,bill_date,due_date,units,previous_due,current_bill,payable_amount) 
  values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
  values = (bill_no,consumer_no,bill_month,bill_date,due_date,units,previous_due,current_bill,payable_amount)
  cursor.execute(query,values)
  conn.commit()
  
  cursor.execute("""select * from consumers where consumer_no = %s""",(consumer_no,))
  consumer = cursor.fetchone()
  
  bill = {
    "bill_no": bill_no,
    "bill_month": bill_month,
    "bill_date": bill_date,
    "due_date": due_date,

    "consumer_no": consumer["consumer_no"],
    "consumer_name": consumer["consumer_name"],
    "address": consumer["address"],
    "mobile": consumer["mobile"],
    "email": consumer["email"],
    "division": consumer["division"],
    "meter_no": consumer["meter_no"],
    "connection_date": consumer["connection_date"],
    "sanctioned_load": consumer["sanctioned_load"],

    "units": units,
    "current_bill": current_bill,
    "previous_due": previous_due,
    "payable_amount": payable_amount
}
  return render_template(
  "bill.html",
  bill = bill,
  pdf_mode = False
  )
  
  
  
@app.route('/download_pdf/<bill_no>')
def download_pdf(bill_no):
  
  conn = get_connection()
  cursor = conn.cursor(dictionary = True)
  
  cursor.execute("""
    select b.*, c.consumer_name, c.address, c.mobile, c.email, c.division, c.meter_no, c.connection_date, c.sanctioned_load
    from bills b
    join consumers c
    on b.consumer_no = c.consumer_no
    where b.bill_no = %s""",(bill_no,))
  
  bill = cursor.fetchone()
  
  html = render_template(
    "bill.html",
    bill=bill,
    pdf_mode = True
    )
  
  pdf = pdfkit.from_string(
    html,
    False,
    configuration=config,
    css="static/css/style.css",
    options={
        "enable-local-file-access": ""
    }
)
  
  response = make_response(pdf)
  response.headers["Content-Type"] = "application/pdf"
  response.headers["Content-Disposition"] = (
    f"attachment; filename={bill_no}.pdf")
  
  return response


  
if __name__ =="__main__":
  app.run(debug=True)
  