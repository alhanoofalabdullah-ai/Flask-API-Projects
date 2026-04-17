
---

# 💻 3️⃣ app.py

```python
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
FILE_NAME = "users.json"


def load_users():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_users(users):
    with open(FILE_NAME, "w") as f:
        json.dump(users, f, indent=4)


def generate_id(users):
    return max([u["id"] for u in users], default=0) + 1


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password required"}), 400

    users = load_users()

    # Check duplicate
    for u in users:
        if u["username"] == data["username"]:
            return jsonify({"error": "User already exists"}), 400

    new_user = {
        "id": generate_id(users),
        "username": data["username"],
        "password": data["password"]
    }

    users.append(new_user)
    save_users(users)

    return jsonify({"message": "User registered successfully"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    users = load_users()

    for u in users:
        if u["username"] == data.get("username") and u["password"] == data.get("password"):
            return jsonify({"message": "Login successful"})

    return jsonify({"error": "Invalid credentials"}), 401


if __name__ == "__main__":
    app.run(debug=True)
