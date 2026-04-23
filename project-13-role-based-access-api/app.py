
# app.py

```python
import sqlite3
import datetime
from functools import wraps

import jwt
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config["SECRET_KEY"] = "supersecretkey"
DATABASE = "database.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def generate_token(user_id, username, role):
    payload = {
        "user_id": user_id,
        "username": username,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }

    return jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"error": "Authorization header is missing"}), 401

        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Invalid authorization format"}), 401

        token = auth_header.split(" ")[1]

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            request.user = data
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

        return func(*args, **kwargs)

    return decorated


def role_required(required_role):
    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            if request.user["role"] != required_role:
                return jsonify({"error": "Access denied"}), 403
            return func(*args, **kwargs)
        return decorated
    return decorator


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Role-Based Access API is running"}), 200


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    username = data.get("username", "").strip()
    password = data.get("password", "").strip()
    role = data.get("role", "user").strip().lower()

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if role not in ["admin", "user"]:
        return jsonify({"error": "Role must be admin or user"}), 400

    if len(username) < 3:
        return jsonify({"error": "Username must be at least 3 characters"}), 400

    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters"}), 400

    hashed_password = generate_password_hash(password)
    created_at = datetime.datetime.utcnow().isoformat()

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password, role, created_at) VALUES (?, ?, ?, ?)",
            (username, hashed_password, role, created_at)
        )
        conn.commit()
        user_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"error": "Username already exists"}), 409

    conn.close()

    return jsonify({
        "message": "User registered successfully",
        "user": {
            "id": user_id,
            "username": username,
            "role": role,
            "created_at": created_at
        }
    }), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if not user:
        return jsonify({"error": "Invalid username or password"}), 401

    if not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid username or password"}), 401

    token = generate_token(user["id"], user["username"], user["role"])

    return jsonify({
        "message": "Login successful",
        "token": token
    }), 200


@app.route("/profile", methods=["GET"])
@token_required
def profile():
    return jsonify({
        "message": "Protected profile data",
        "user": {
            "id": request.user["user_id"],
            "username": request.user["username"],
            "role": request.user["role"]
        }
    }), 200


@app.route("/admin", methods=["GET"])
@token_required
@role_required("admin")
def admin_dashboard():
    return jsonify({
        "message": "Welcome to the admin dashboard",
        "user": request.user["username"]
    }), 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
