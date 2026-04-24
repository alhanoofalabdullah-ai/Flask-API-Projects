import sqlite3
import logging
from datetime import datetime
from flask import Flask, request, jsonify, g

app = Flask(__name__)

DATABASE = "database.db"

logging.basicConfig(
    filename="api.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


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
            category TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS request_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            method TEXT NOT NULL,
            path TEXT NOT NULL,
            status_code INTEGER,
            timestamp TEXT NOT NULL
        )
    """)

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


def error_response(message, status_code):
    return jsonify({
        "success": False,
        "error": {
            "message": message,
            "status_code": status_code
        }
    }), status_code


def save_request_log(method, path, status_code):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO request_logs (method, path, status_code, timestamp)
        VALUES (?, ?, ?, ?)
        """,
        (method, path, status_code, datetime.utcnow().isoformat())
    )

    conn.commit()
    conn.close()


@app.before_request
def before_request():
    g.start_time = datetime.utcnow()
    logging.info(f"Incoming request: {request.method} {request.path}")


@app.after_request
def after_request(response):
    save_request_log(request.method, request.path, response.status_code)
    logging.info(
        f"Completed request: {request.method} {request.path} "
        f"Status: {response.status_code}"
    )
    return response


@app.route("/", methods=["GET"])
def home():
    return success_response("API Logging and Request Tracking is running")


@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()

    if not data:
        return error_response("Request body is required", 400)

    name = data.get("name", "").strip()
    category = data.get("category", "").strip()

    if not name or not category:
        return error_response("Name and category are required", 400)

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO items (name, category) VALUES (?, ?)",
        (name, category)
    )

    conn.commit()
    item_id = cursor.lastrowid
    conn.close()

    item = {
        "id": item_id,
        "name": name,
        "category": category
    }

    return success_response("Item created successfully", item, 201)


@app.route("/items", methods=["GET"])
def get_items():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items ORDER BY id")
    rows = cursor.fetchall()
    conn.close()

    items = [
        {
            "id": row["id"],
            "name": row["name"],
            "category": row["category"]
        }
        for row in rows
    ]

    return success_response("Items retrieved successfully", items)


@app.route("/logs", methods=["GET"])
def get_logs():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM request_logs ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()

    logs = [
        {
            "id": row["id"],
            "method": row["method"],
            "path": row["path"],
            "status_code": row["status_code"],
            "timestamp": row["timestamp"]
        }
        for row in rows
    ]

    return success_response("Request logs retrieved successfully", logs)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
