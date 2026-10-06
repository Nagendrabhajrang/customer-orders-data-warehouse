# Customer Orders Data Warehouse for Business Insights

A simple Data Analytics project using:

- Python
- Flask
- SQL (SQLite for easy setup)
- Pandas
- HTML/CSS
- Chart.js

## Project flow

Customer/Order Data
        ↓
SQL Database
        ↓
Flask + Python
        ↓
SQL Queries
        ↓
HTML Dashboard
        ↓
Interactive Charts + Business Insights

## Tools required

1. Python 3.10+
2. VS Code (recommended)
3. Flask
4. Pandas
5. SQLite (included with Python)
6. Any modern web browser

## Installation

Open terminal inside the project folder:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

## Create the database

Run:

```bash
python init_db.py
```

This creates:

```text
database/customer_orders.db
```

## Run the Flask application

```bash
python run.py
```

Open:

```text
http://127.0.0.1:5000
```

## Main business questions answered

- How many customers are there?
- How many orders are there?
- What is total sales?
- Which product categories generate more sales?
- Which products have higher sales?
- How many orders are delivered, pending or cancelled?
- What are the recent orders?

## Future extensions

- MySQL instead of SQLite
- CSV upload
- Login system
- Customer search/filter
- Date filters
- Power BI dashboard
- Export reports to Excel/PDF
- Predictive sales analysis
