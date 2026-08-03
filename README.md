# ⚡ Electricity Bill Generator

A web-based Electricity Bill Generator developed using **Python Flask** and **MySQL**. The application allows users to search for consumers, generate electricity bills based on units consumed, store bill records in a database, and download bills as PDF files.

---

## 📌 Features

- Search consumer using Consumer Number
- Display consumer details
- Calculate electricity bill using slab-wise rates
- Maintain previous due amount
- Store generated bills in MySQL
- Generate and display electricity bill
- Download bill as PDF
- Clean and user-friendly interface

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Flask | Web framework |
| HTML5 | Web page structure |
| CSS3 | User interface styling |
| MySQL | Database management |
| MySQL Connector | Database connectivity |
| Jinja2 | Dynamic HTML templates |
| pdfkit | PDF generation |
| wkhtmltopdf | Convert HTML to PDF |
| VS Code | Code editor |
| Git & GitHub | Version control |

---

## 📚 My Knowledge & Usage

### Python (Intermediate)
- Functions
- Conditional statements
- Loops
- Dictionaries
- Database connectivity
- Modules

Used for implementing the billing logic, database operations, and backend functionality.

### Flask (Intermediate)
- Routing
- GET & POST requests
- Template rendering
- Form handling
- Dynamic data passing

Used to develop the complete web application.

### HTML & CSS (Intermediate)
- Forms
- Tables
- Buttons
- Responsive layouts
- Styling
- Print-friendly pages

Used to design all web pages and the downloadable bill.

### MySQL (Intermediate)
- Database creation
- Tables
- INSERT
- SELECT
- UPDATE
- Foreign Keys

Used to store consumer details and generated bills.

### MySQL Connector (Basic–Intermediate)
Used to connect the Flask application with the MySQL database.

### Jinja2 (Intermediate)
Used for rendering dynamic data in HTML templates using Flask.

### pdfkit & wkhtmltopdf (Basic)
Used for generating downloadable PDF bills from HTML pages.

### Git & GitHub (Basic)
Used for version control and project management.

---

## 🗄️ Database

### Consumers Table

Stores consumer information:

- Consumer Number
- Consumer Name
- Address
- Mobile Number
- Email
- Division
- Meter Number
- Sanctioned Load
- Connection Date

### Bills Table

Stores generated bill information:

- Bill Number
- Consumer Number
- Bill Month
- Bill Date
- Due Date
- Units Consumed
- Previous Due
- Current Bill
- Total Payable Amount

---

## ⚡ Billing Logic

The application calculates electricity charges based on slab rates.

| Units | Rate |
|-------:|------:|
| 0 – 50 | ₹1.75 / unit |
| 51 – 100 | ₹3.00 / unit |
| 101 – 150 | ₹4.25 / unit |
| 151 – 200 | ₹5.50 / unit |
| Above 200 | ₹7.50 / unit |

The previous due amount is added to the current bill to calculate the total payable amount.

---

## 🔄 Project Workflow

1. Search consumer using Consumer Number.
2. Fetch consumer details from MySQL.
3. Enter units consumed.
4. Calculate electricity bill.
5. Store bill details in the database.
6. Display generated bill.
7. Download bill as PDF.

---

## 📂 Project Structure

```
Electricity_Bill/
│
├── app.py
├── database.py
├── static/
│   ├── css/
│   └── images/
├── templates/
│   ├── index.html
│   ├── consumer.html
│   └── bill.html
└── README.md
```

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Building web applications using Flask
- Connecting Python with MySQL
- Creating dynamic web pages using Jinja2
- Implementing slab-based bill calculation
- Generating PDF documents from HTML
- Designing responsive user interfaces with HTML and CSS
- Managing project versions using Git and GitHub

---

## 📌 Conclusion

The **Electricity Bill Generator** automates electricity bill generation through a simple and efficient web interface. It demonstrates the integration of Python Flask, MySQL, HTML, CSS, and PDF generation while providing practical experience in full-stack web application development.
