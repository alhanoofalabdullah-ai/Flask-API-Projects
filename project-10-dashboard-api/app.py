
---

# 💻 3️⃣ app.py (🔥 أقوى كود)

```python
from flask import Flask, jsonify
import json
import os

app = Flask(__name__)
FILE_NAME = "data.json"


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


@app.route("/dashboard", methods=["GET"])
def full_dashboard():
    data = load_data()

    total = sum(d["amount"] for d in data)
    count = len(data)

    category = {}
    for d in data:
        category[d["category"]] = category.get(d["category"], 0) + d["amount"]

    top = max(data, key=lambda x: x["amount"]) if data else {}

    return jsonify({
        "total": total,
        "count": count,
        "category": category,
        "top": top
    })


@app.route("/dashboard/total", methods=["GET"])
def total():
    data = load_data()
    return jsonify({"total": sum(d["amount"] for d in data)})


@app.route("/dashboard/count", methods=["GET"])
def count():
    data = load_data()
    return jsonify({"count": len(data)})


@app.route("/dashboard/category", methods=["GET"])
def category():
    data = load_data()
    result = {}

    for d in data:
        result[d["category"]] = result.get(d["category"], 0) + d["amount"]

    return jsonify(result)


@app.route("/dashboard/top", methods=["GET"])
def top():
    data = load_data()

    if not data:
        return jsonify({"message": "No data"})

    return jsonify(max(data, key=lambda x: x["amount"]))


if __name__ == "__main__":
    app.run(debug=True)
