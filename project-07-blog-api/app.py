
---

# 💻 3️⃣ app.py

```python
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
FILE_NAME = "posts.json"


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


@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify(load_data())


@app.route("/posts", methods=["POST"])
def add_post():
    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({"error": "Title required"}), 400

    posts = load_data()

    new_post = {
        "id": generate_id(posts),
        "title": data.get("title"),
        "content": data.get("content", ""),
        "comments": []
    }

    posts.append(new_post)
    save_data(posts)

    return jsonify(new_post), 201


@app.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    posts = load_data()
    updated = [p for p in posts if p["id"] != post_id]

    if len(updated) == len(posts):
        return jsonify({"error": "Not found"}), 404

    save_data(updated)
    return jsonify({"message": "Deleted"})


@app.route("/posts/<int:post_id>/comments", methods=["POST"])
def add_comment(post_id):
    data = request.get_json()
    posts = load_data()

    for p in posts:
        if p["id"] == post_id:
            comment = {
                "text": data.get("text", "")
            }
            p["comments"].append(comment)
            save_data(posts)
            return jsonify(comment), 201

    return jsonify({"error": "Post not found"}), 404


@app.route("/posts/<int:post_id>/comments", methods=["GET"])
def get_comments(post_id):
    posts = load_data()

    for p in posts:
        if p["id"] == post_id:
            return jsonify(p["comments"])

    return jsonify({"error": "Post not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
