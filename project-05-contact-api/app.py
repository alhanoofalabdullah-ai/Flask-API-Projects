
---

# 💻 3️⃣ app.py

```python
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
FILE_NAME = "contacts.json"


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


def generate_id(data):
    return max([c["id"] for c in data], default=0) + 1


@app.route("/contacts", methods=["GET"])
def get_contacts():
    return jsonify(load_data())


@app.route("/contacts", methods=["POST"])
def add_contact():
    data = request.get_json()

    if not data or not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    contacts = load_data()

    new_contact = {
        "id": generate_id(contacts),
        "name": data.get("name"),
        "phone": data.get("phone", ""),
        "email": data.get("email", "")
    }

    contacts.append(new_contact)
    save_data(contacts)

    return jsonify(new_contact), 201


@app.route("/contacts/<int:contact_id>", methods=["PUT"])
def update_contact(contact_id):
    data = request.get_json()
    contacts = load_data()

    for c in contacts:
        if c["id"] == contact_id:
            c["name"] = data.get("name", c["name"])
            c["phone"] = data.get("phone", c["phone"])
            c["email"] = data.get("email", c["email"])
            save_data(contacts)
            return jsonify(c)

    return jsonify({"error": "Not found"}), 404


@app.route("/contacts/<int:contact_id>", methods=["DELETE"])
def delete_contact(contact_id):
    contacts = load_data()
    updated = [c for c in contacts if c["id"] != contact_id]

    if len(updated) == len(contacts):
        return jsonify({"error": "Not found"}), 404

    save_data(updated)
    return jsonify({"message": "Deleted"})


@app.route("/contacts/search", methods=["GET"])
def search_contacts():
    keyword = request.args.get("q", "").lower()
    contacts = load_data()

    results = [c for c in contacts if keyword in c["name"].lower()]
    return jsonify(results)


@app.route("/contacts/filter", methods=["GET"])
def filter_contacts():
    email = request.args.get("email", "").lower()
    contacts = load_data()

    results = [c for c in contacts if email in c["email"].lower()]
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
