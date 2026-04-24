import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

DATABASE = "database.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def error_response(message, status_code):
    return jsonify({
        "success": False,
        "error": {
            "message": message,
            "status_code": status_code
        }
    }), status_code


def success_response(message, data=None, status_code=200):
    response = {
        "success": True,
        "message": message
    }

    if data is not None:
        response["data"] = data

    return jsonify(response), status_code


def validate_product_data(data):
    if not data:
        return "Request body is required"

    name = data.get("name")
    category = data.get("category")
    price = data.get("price")

    if not name or not isinstance(name, str):
        return "Product name is required and must be a string"

    if not category or not isinstance(category, str):
        return "Product category is required and must be a string"

    if price is None:
        return "Product price is required"

    if not isinstance(price, (int, float)):
        return "Product price must be a number"

    if price <= 0:
        return "Product price must be greater than zero"

    return None


@app.errorhandler(404)
def not_found(error):
    return error_response("Resource not found", 404)


@app.errorhandler(500)
def internal_error(error):
    return error_response("Internal server error", 500)


@app.route("/", methods=["GET"])
def home():
    return success_response("API Error Handling and Validation is running")


@app.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()

    validation_error = validate_product_data(data)

    if validation_error:
        return error_response(validation_error, 400)

    name = data["name"].strip()
    category = data["category"].strip()
    price = data["price"]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products (name, category, price) VALUES (?, ?, ?)",
        (name, category, price)
    )

    conn.commit()
    product_id = cursor.lastrowid
    conn.close()

    product = {
        "id": product_id,
        "name": name,
        "category": category,
        "price": price
    }

    return success_response("Product created successfully", product, 201)


@app.route("/products", methods=["GET"])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products ORDER BY id")
    rows = cursor.fetchall()
    conn.close()

    products = [
        {
            "id": row["id"],
            "name": row["name"],
            "category": row["category"],
            "price": row["price"]
        }
        for row in rows
    ]

    return success_response("Products retrieved successfully", products)


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return error_response("Product not found", 404)

    product = {
        "id": row["id"],
        "name": row["name"],
        "category": row["category"],
        "price": row["price"]
    }

    return success_response("Product retrieved successfully", product)


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    row = cursor.fetchone()

    if not row:
        conn.close()
        return error_response("Product not found", 404)

    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

    return success_response("Product deleted successfully")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
