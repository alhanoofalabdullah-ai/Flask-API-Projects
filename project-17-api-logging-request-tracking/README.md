# API Logging and Request Tracking

A professional Flask API project focused on logging requests, tracking API activity, and monitoring endpoint usage.

---

## Overview

This project demonstrates how to implement request logging and tracking in a Flask API using Python logging and SQLite.

---

## Features

- Log incoming requests
- Track request method and path
- Store request logs in SQLite
- Track response status codes
- View API request history
- Return structured JSON responses

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- database.db → SQLite database
- api.log → Log file
- README.md → Project documentation

---

## Endpoints

### Health Check
GET /

### Create Item
POST /items

### Get Items
GET /items

### Get Request Logs
GET /logs

---

## Technologies Used

- Python
- Flask
- SQLite
- Logging
- REST API
- Request Tracking

## Setup Commands

- cd ~/Flask-API-Projects
- mkdir project-17-api-logging-request-tracking
- cd project-17-api-logging-request-tracking
- touch README.md app.py requirements.txt api.log

## Run

- pip install -r requirements.txt
- python app.py

## Git Commands

- cd ..
- git add .
- git commit -m "add project 17 api logging request tracking"
- git push

## Testing Examples

- GET http://127.0.0.1:5000/
- POST http://127.0.0.1:5000/items

{
  "name": "Laptop",
  "category": "Electronics"
}

- GET http://127.0.0.1:5000/items
- GET http://127.0.0.1:5000/logs


---

## Author

Alhanoof Alabdullah
