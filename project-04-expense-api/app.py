
---

# 💻 3️⃣ app.py

```python
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
FILE_NAME = "expenses.json"


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


def generate_id(data):
    return max([e["id"] for e in data], default=0) + 1


@app.route("/expenses", methods=["GET"])
def get_expenses():
    return jsonify(load_data())


@app.route("/expenses", methods=["POST"])
def add_expense():
    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400

    expenses = load_data()

    new_expense = {
        "id": generate_id(expenses),
        "title": data.get("title"),
        "amount": data.get("amount", 0),
        "category": data.get("category", "general")
    }

    expenses.append(new_expense)
    save_data(expenses)

    return jsonify(new_expense), 201


@app.route("/expenses/<int:expense_id>", methods=["DELETE"])
def delete_expense(expense_id):
    expenses = load_data()
    updated = [e for e in expenses if e["id"] != expense_id]

    if len(updated) == len(expenses):
        return jsonify({"error": "Not found"}), 404

    save_data(updated)
    return jsonify({"message": "Deleted"})


@app.route("/expenses/search", methods=["GET"])
def search_expenses():
    keyword = request.args.get("q", "").lower()
    expenses = load_data()

    results = [e for e in expenses if keyword in e["title"].lower()]
    return jsonify(results)


@app.route("/expenses/filter", methods=["GET"])
def filter_expenses():
    category = request.args.get("category", "").lower()
    expenses = load_data()

    results = [e for e in expenses if e["category"].lower() == category]
    return jsonify(results)


@app.route("/expenses/total", methods=["GET"])
def total_expenses():
    expenses = load_data()
    total = sum(e["amount"] for e in expenses)

    return jsonify({"total": total})


@app.route("/expenses/report", methods=["GET"])
def report():
    expenses = load_data()
    report_data = {}

    for e in expenses:
        cat = e["category"]
        report_data[cat] = report_data.get(cat, 0) + e["amount"]

    return jsonify(report_data)


if __name__ == "__main__":
    app.run(debug=True)
