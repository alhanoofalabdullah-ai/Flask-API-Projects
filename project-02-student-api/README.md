# Student API

A Flask API for managing student records and grades.

## Features
- Add student
- View students
- Update student
- Delete student
- Search students
- Calculate average grades

## Endpoints
- GET /students
- POST /students
- PUT /students/<id>
- DELETE /students/<id>
- GET /students/search?q=name
- GET /students/average/<id>

## Run
```bash
pip install flask
python app.py
