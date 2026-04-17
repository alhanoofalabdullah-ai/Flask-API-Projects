# Task API

A simple Flask REST API for managing tasks.

## Features
- Get all tasks
- Add task
- Update task
- Delete task
- Search tasks
- Filter by status

## Endpoints
- GET /tasks
- POST /tasks
- PUT /tasks/<id>
- DELETE /tasks/<id>
- GET /tasks/search?q=keyword
- GET /tasks/filter?status=pending

## How to Run
```bash
pip install flask
python app.py
