
---

# 💻 3️⃣ app.py

```python
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
FILE_NAME = "store.json"


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {"products": [], "orders": []}


def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


def generate_id(items):
    return max([i["id"] for i in items], default=0) + 1


@app.route("/products", methods=["GET"])
def get_products():
    data = load_data()
    return jsonify(data["products"])


@app.route("/products", methods=["POST"])
def add_product():
    req = request.get_json()
    data = load_data()

    if not req or not req.get("name"):
        return jsonify({"error": "Name required"}), 400

    product = {
        "id": generate_id(data["products"]),
        "name": req.get("name"),
        "price": req.get("price", 0)
    }

    data["products"].append(product)
    save_data(data)

    return jsonify(product), 201


@app.route("/orders", methods=["POST"])
def create_order():
    req = request.get_json()
    data = load_data()

    product_ids = req.get("products", [])
    products = data["products"]

    selected = [p for p in products if p["id"] in product_ids]

    if not selected:
        return jsonify({"error": "No valid products"}), 400

    total = sum(p["price"] for p in selected)

    order = {
        "id": generate_id(data["orders"]),
        "products": selected,
        "total": total
    }

    data["orders"].append(order)
    save_data(data)

    return jsonify(order), 201


@app.route("/orders", methods=["GET"])
def get_orders():
    data = load_data()
    return jsonify(data["orders"])


if __name__ == "__main__":
    app.run(debug=True)
