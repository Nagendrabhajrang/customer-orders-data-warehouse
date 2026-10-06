from flask import Blueprint, render_template, jsonify
from .db import get_db

main = Blueprint("main", __name__)

@main.route("/")
def dashboard():
    db = get_db()

    total_customers = db.execute(
        "SELECT COUNT(*) FROM customers"
    ).fetchone()[0]

    total_orders = db.execute(
        "SELECT COUNT(*) FROM orders"
    ).fetchone()[0]

    total_sales = db.execute("""
        SELECT COALESCE(SUM(od.quantity * od.unit_price), 0)
        FROM order_details od
        JOIN orders o ON od.order_id = o.order_id
        WHERE o.order_status != 'Cancelled'
    """).fetchone()[0]

    delivered_orders = db.execute("""
        SELECT COUNT(*) FROM orders
        WHERE order_status = 'Delivered'
    """).fetchone()[0]

    category_sales = db.execute("""
        SELECT p.category,
               SUM(od.quantity * od.unit_price) AS sales
        FROM order_details od
        JOIN products p ON od.product_id = p.product_id
        JOIN orders o ON od.order_id = o.order_id
        WHERE o.order_status != 'Cancelled'
        GROUP BY p.category
        ORDER BY sales DESC
    """).fetchall()

    product_sales = db.execute("""
        SELECT p.product_name,
               SUM(od.quantity * od.unit_price) AS sales
        FROM order_details od
        JOIN products p ON od.product_id = p.product_id
        JOIN orders o ON od.order_id = o.order_id
        WHERE o.order_status != 'Cancelled'
        GROUP BY p.product_id, p.product_name
        ORDER BY sales DESC
        LIMIT 5
    """).fetchall()

    status_data = db.execute("""
        SELECT order_status, COUNT(*) AS count
        FROM orders
        GROUP BY order_status
    """).fetchall()

    recent_orders = db.execute("""
        SELECT o.order_id, c.customer_name,
               o.order_date, o.order_status,
               SUM(od.quantity * od.unit_price) AS amount
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        JOIN order_details od ON o.order_id = od.order_id
        GROUP BY o.order_id, c.customer_name,
                 o.order_date, o.order_status
        ORDER BY o.order_date DESC
        LIMIT 10
    """).fetchall()

    db.close()

    return render_template(
        "dashboard.html",
        total_customers=total_customers,
        total_orders=total_orders,
        total_sales=total_sales,
        delivered_orders=delivered_orders,
        category_sales=category_sales,
        product_sales=product_sales,
        status_data=status_data,
        recent_orders=recent_orders
    )

@main.route("/api/category-sales")
def category_sales_api():
    db = get_db()
    rows = db.execute("""
        SELECT p.category,
               SUM(od.quantity * od.unit_price) AS sales
        FROM order_details od
        JOIN products p ON od.product_id = p.product_id
        JOIN orders o ON od.order_id = o.order_id
        WHERE o.order_status != 'Cancelled'
        GROUP BY p.category
    """).fetchall()
    db.close()

    return jsonify([
        {"category": row["category"], "sales": row["sales"]}
        for row in rows
    ])
