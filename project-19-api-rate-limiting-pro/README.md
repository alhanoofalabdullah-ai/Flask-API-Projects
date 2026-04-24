# API Rate Limiting Pro

A professional Flask API project focused on limiting API requests to protect services from abuse and excessive traffic.

---

## Overview

This project demonstrates how to implement API rate limiting using Flask and in-memory request tracking.

---

## Features

- Limit requests per client IP
- Track request timestamps
- Return 429 status code when limit is exceeded
- Protect selected endpoints
- Structured JSON responses
- Simple in-memory rate limiter

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- README.md → Project documentation

---

## Endpoints

### Health Check
GET /

### Public Data
GET /data

---

## Technologies Used

- Python
- Flask
- REST API
- Rate Limiting
- Request Tracking

## Setup Commands

- cd ~/Flask-API-Projects
- mkdir project-19-api-rate-limiting-pro
- cd project-19-api-rate-limiting-pro
- touch README.md app.py requirements.txt

## Run

- pip install -r requirements.txt
- python app.py

## Git Commands

- cd ..
- git add .
- git commit -m "add project 19 api rate limiting pro"
- git push

## Testing Examples

- GET http://127.0.0.1:5000/
- GET http://127.0.0.1:5000/data

{
  "success": false,
  "error": {
    "message": "Rate limit exceeded. Please try again later.",
    "status_code": 429
  }
}

---

## Author

Alhanoof Alabdullah
