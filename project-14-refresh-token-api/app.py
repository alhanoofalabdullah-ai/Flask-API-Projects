
---

## app.py

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
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def generate_access_token(user_id, username):
    payload = {
        "user_id": user_id,
        "username": username,
        "type": "access",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    }

    return jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")


def generate_refresh_token(user_id, username):
    payload = {
        "user_id": user_id,
        "username": username,
        "type": "refresh",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
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

            if data.get("type") != "access":
                return jsonify({"error": "Invalid access token"}), 401

            request.user = data
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Access token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

        return func(*args, **kwargs)

    return decorated


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Refresh Token API is running"}), 200


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

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
            "INSERT INTO users (username, password, created_at) VALUES (?, ?, ?)",
            (username, hashed_password, created_at)
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

    access_token = generate_access_token(user["id"], user["username"])
    refresh_token = generate_refresh_token(user["id"], user["username"])

    return jsonify({
        "message": "Login successful",
        "access_token": access_token,
        "refresh_token": refresh_token
    }), 200


@app.route("/refresh", methods=["POST"])
def refresh():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    refresh_token = data.get("refresh_token", "").strip()

    if not refresh_token:
        return jsonify({"error": "Refresh token is required"}), 400

    try:
        data = jwt.decode(refresh_token, app.config["SECRET_KEY"], algorithms=["HS256"])

        if data.get("type") != "refresh":
            return jsonify({"error": "Invalid refresh token"}), 401

        new_access_token = generate_access_token(data["user_id"], data["username"])

        return jsonify({
            "message": "Access token refreshed successfully",
            "access_token": new_access_token
        }), 200

    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Refresh token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid refresh token"}), 401


@app.route("/profile", methods=["GET"])
@token_required
def profile():
    return jsonify({
        "message": "Protected profile data",
        "user": {
            "id": request.user["user_id"],
            "username": request.user["username"]
        }
    }), 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
