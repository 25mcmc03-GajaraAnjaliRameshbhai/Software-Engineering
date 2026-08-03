import mysql.connector

def get_connection():
  
  conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "password",
    database = "electricity_bill"
  )
  
  return conn