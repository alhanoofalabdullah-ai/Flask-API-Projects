
---

# 💻 3️⃣ app.py

```python
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
FILE_NAME = "students.json"


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


def generate_id(data):
    return max([s["id"] for s in data], default=0) + 1


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(load_data())


@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    if not data or not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    students = load_data()

    new_student = {
        "id": generate_id(students),
        "name": data.get("name"),
        "grades": data.get("grades", [])
    }

    students.append(new_student)
    save_data(students)

    return jsonify(new_student), 201


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()
    students = load_data()

    for s in students:
        if s["id"] == student_id:
            s["name"] = data.get("name", s["name"])
            s["grades"] = data.get("grades", s["grades"])
            save_data(students)
            return jsonify(s)

    return jsonify({"error": "Student not found"}), 404


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    students = load_data()
    updated = [s for s in students if s["id"] != student_id]

    if len(updated) == len(students):
        return jsonify({"error": "Student not found"}), 404

    save_data(updated)
    return jsonify({"message": "Deleted"})


@app.route("/students/search", methods=["GET"])
def search_students():
    keyword = request.args.get("q", "").lower()
    students = load_data()

    results = [s for s in students if keyword in s["name"].lower()]
    return jsonify(results)


@app.route("/students/average/<int:student_id>", methods=["GET"])
def average(student_id):
    students = load_data()

    for s in students:
        if s["id"] == student_id:
            if not s["grades"]:
                return jsonify({"average": 0})

            avg = sum(s["grades"]) / len(s["grades"])
            return jsonify({"average": avg})

    return jsonify({"error": "Student not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
