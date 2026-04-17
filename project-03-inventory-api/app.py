
---

# 💻 3️⃣ app.py

```python
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
FILE_NAME = "inventory.json"


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


def generate_id(data):
    return max([p["id"] for p in data], default=0) + 1


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(load_data())


@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()

    if not data or not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    products = load_data()

    new_product = {
        "id": generate_id(products),
        "name": data.get("name"),
        "price": data.get("price", 0),
        "stock": data.get("stock", 0)
    }

    products.append(new_product)
    save_data(products)

    return jsonify(new_product), 201


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()
    products = load_data()

    for p in products:
        if p["id"] == product_id:
            p["name"] = data.get("name", p["name"])
            p["price"] = data.get("price", p["price"])
            p["stock"] = data.get("stock", p["stock"])
            save_data(products)
            return jsonify(p)

    return jsonify({"error": "Product not found"}), 404


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    products = load_data()
    updated = [p for p in products if p["id"] != product_id]

    if len(updated) == len(products):
        return jsonify({"error": "Product not found"}), 404

    save_data(updated)
    return jsonify({"message": "Deleted"})


@app.route("/products/search", methods=["GET"])
def search_products():
    keyword = request.args.get("q", "").lower()
    products = load_data()

    results = [p for p in products if keyword in p["name"].lower()]
    return jsonify(results)


@app.route("/products/filter", methods=["GET"])
def filter_products():
    level = request.args.get("stock")

    products = load_data()

    if level == "low":
        results = [p for p in products if p["stock"] < 5]
    else:
        results = products

    return jsonify(results)


@app.route("/products/value", methods=["GET"])
def total_value():
    products = load_data()
    total = sum(p["price"] * p["stock"] for p in products)

    return jsonify({"total_value": total})


if __name__ == "__main__":
    app.run(debug=True)
