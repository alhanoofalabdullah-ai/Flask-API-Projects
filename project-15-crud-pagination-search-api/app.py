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
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "CRUD API with Pagination and Search is running"}), 200


@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get("name", "").strip()
    category = data.get("category", "").strip()
    price = data.get("price")

    if not name or not category or price is None:
        return jsonify({"error": "Name, category, and price are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO items (name, category, price) VALUES (?, ?, ?)",
        (name, category, price)
    )

    conn.commit()
    item_id = cursor.lastrowid
    conn.close()

    return jsonify({
        "message": "Item created successfully",
        "item": {
            "id": item_id,
            "name": name,
            "category": category,
            "price": price
        }
    }), 201


@app.route("/items", methods=["GET"])
def get_items():
    page = request.args.get("page", default=1, type=int)
    limit = request.args.get("limit", default=5, type=int)
    search = request.args.get("search", default="", type=str)

    if page < 1:
        page = 1

    if limit < 1:
        limit = 5

    offset = (page - 1) * limit

    conn = get_db_connection()
    cursor = conn.cursor()

    if search:
        cursor.execute(
            "SELECT COUNT(*) FROM items WHERE name LIKE ?",
            (f"%{search}%",)
        )
        total_items = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT * FROM items
            WHERE name LIKE ?
            ORDER BY id
            LIMIT ? OFFSET ?
            """,
            (f"%{search}%", limit, offset)
        )
    else:
        cursor.execute("SELECT COUNT(*) FROM items")
        total_items = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT * FROM items
            ORDER BY id
            LIMIT ? OFFSET ?
            """,
            (limit, offset)
        )

    rows = cursor.fetchall()
    conn.close()

    items = [
        {
            "id": row["id"],
            "name": row["name"],
            "category": row["category"],
            "price": row["price"]
        }
        for row in rows
    ]

    return jsonify({
        "page": page,
        "limit": limit,
        "total_items": total_items,
        "items": items
    }), 200


@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return jsonify({"error": "Item not found"}), 404

    return jsonify({
        "id": row["id"],
        "name": row["name"],
        "category": row["category"],
        "price": row["price"]
    }), 200


@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get("name", "").strip()
    category = data.get("category", "").strip()
    price = data.get("price")

    if not name or not category or price is None:
        return jsonify({"error": "Name, category, and price are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    existing_item = cursor.fetchone()

    if not existing_item:
        conn.close()
        return jsonify({"error": "Item not found"}), 404

    cursor.execute(
        """
        UPDATE items
        SET name = ?, category = ?, price = ?
        WHERE id = ?
        """,
        (name, category, price, item_id)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Item updated successfully"}), 200


@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    existing_item = cursor.fetchone()

    if not existing_item:
        conn.close()
        return jsonify({"error": "Item not found"}), 404

    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Item deleted successfully"}), 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
