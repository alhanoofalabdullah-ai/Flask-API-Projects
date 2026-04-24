import sqlite3
import time
from flask import Flask, jsonify

app = Flask(__name__)

DATABASE = "database.db"

cache = {}
CACHE_DURATION = 30


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

    cursor.execute("SELECT COUNT(*) FROM products")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany(
            "INSERT INTO products (name, category, price) VALUES (?, ?, ?)",
            [
                ("Laptop", "Electronics", 3500),
                ("Phone", "Electronics", 2200),
                ("Desk", "Furniture", 900),
                ("Chair", "Furniture", 450),
                ("Headphones", "Electronics", 300)
            ]
        )

    conn.commit()
    conn.close()


def success_response(message, data=None, status_code=200):
    response = {
        "success": True,
        "message": message
    }

    if data is not None:
        response["data"] = data

    return jsonify(response), status_code


@app.route("/", methods=["GET"])
def home():
    return success_response("API Caching Pro is running")


@app.route("/products", methods=["GET"])
def get_products():
    cache_key = "products"

    if cache_key in cache:
        cached_data = cache[cache_key]

        if time.time() - cached_data["timestamp"] < CACHE_DURATION:
            return success_response(
                "Products retrieved from cache",
                cached_data["data"]
            )

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

    cache[cache_key] = {
        "timestamp": time.time(),
        "data": products
    }

    return success_response("Products retrieved from database", products)


@app.route("/cache", methods=["DELETE"])
def clear_cache():
    cache.clear()
    return success_response("Cache cleared successfully")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
