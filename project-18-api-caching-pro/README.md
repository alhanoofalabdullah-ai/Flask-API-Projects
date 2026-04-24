# API Caching Pro

A professional Flask API project focused on caching API responses to improve performance and reduce repeated processing.

---

## Overview

This project demonstrates how to implement simple in-memory caching in a Flask API using Python dictionaries and expiration time.

---

## Features

- Cache API responses
- Reduce repeated database queries
- Use cache expiration time
- Clear cache manually
- Return structured JSON responses
- SQLite database integration

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- database.db → SQLite database
- README.md → Project documentation

---

## Endpoints

### Health Check
GET /

### Get Products
GET /products

### Clear Cache
DELETE /cache

---

## Technologies Used

- Python
- Flask
- SQLite
- REST API
- In-Memory Caching

## Setup Commands

- cd ~/Flask-API-Projects
- mkdir project-18-api-caching-pro
- cd project-18-api-caching-pro
- touch README.md app.py requirements.txt

## Run

- pip install -r requirements.txt
- python app.py

## Git Commands

- cd ..
- git add .
- git commit -m "add project 18 api caching pro"
- git push

## Testing Examples

- GET http://127.0.0.1:5000/
- GET http://127.0.0.1:5000/products
- DELETE http://127.0.0.1:5000/cache

---

## Author

Alhanoof Alabdullah
