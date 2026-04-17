
---

# 💻 3️⃣ app.py

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


@app.route("/report/total", methods=["GET"])
def total():
    data = load_data()
    total_value = sum(item["amount"] for item in data)

    return jsonify({"total": total_value})


@app.route("/report/category", methods=["GET"])
def category_report():
    data = load_data()
    report = {}

    for item in data:
        cat = item["category"]
        report[cat] = report.get(cat, 0) + item["amount"]

    return jsonify(report)


@app.route("/report/top", methods=["GET"])
def top_item():
    data = load_data()

    if not data:
        return jsonify({"message": "No data"})

    top = max(data, key=lambda x: x["amount"])

    return jsonify(top)


if __name__ == "__main__":
    app.run(debug=True)
