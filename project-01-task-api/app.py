from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)
FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def generate_id(tasks):
    return max([task["id"] for task in tasks], default=0) + 1


@app.route("/")
def home():
    return jsonify({"message": "Task API is running"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400

    tasks = load_tasks()

    new_task = {
        "id": generate_id(tasks),
        "title": data.get("title"),
        "status": data.get("status", "pending"),
        "created_at": datetime.now().isoformat()
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return jsonify(new_task), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data.get("title", task["title"])
            task["status"] = data.get("status", task["status"])
            save_tasks(tasks)
            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]

    if len(updated_tasks) == len(tasks):
        return jsonify({"error": "Task not found"}), 404

    save_tasks(updated_tasks)
    return jsonify({"message": "Task deleted successfully"})


@app.route("/tasks/search", methods=["GET"])
def search_tasks():
    keyword = request.args.get("q", "").lower()
    tasks = load_tasks()

    results = [task for task in tasks if keyword in task["title"].lower()]
    return jsonify(results)


@app.route("/tasks/filter", methods=["GET"])
def filter_tasks():
    status = request.args.get("status", "").lower()
    tasks = load_tasks()

    results = [task for task in tasks if task["status"].lower() == status]
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
