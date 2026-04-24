# API Error Handling and Validation

A professional Flask API project focused on structured error handling and request validation.

---

## Overview

This project demonstrates how to build a Flask API with clean validation rules, custom error responses, and consistent JSON error handling.

---

## Features

- Validate request body
- Validate required fields
- Validate data types
- Handle 404 errors
- Handle 400 errors
- Handle server errors
- Return consistent JSON responses
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

### Create Product
POST /products

### Get Products
GET /products

### Get Product by ID
GET /products/<id>

### Delete Product
DELETE /products/<id>

---

## Technologies Used

- Python
- Flask
- SQLite
- REST API
- Validation
- Error Handling


## Setup Commands

- cd ~/Flask-API-Projects
- mkdir project-16-error-handling-validation-api
- cd project-16-error-handling-validation-api
- touch README.md app.py requirements.txt

## Run

- pip install -r requirements.txt
- python app.py

## Git Commands

- cd ..
- git add .
- git commit -m "add project 16 error handling validation api"
- git push

## Testing Examples

- GET http://127.0.0.1:5000/
- POST http://127.0.0.1:5000/products

{
  "name": "Laptop",
  "category": "Electronics",
  "price": 3500
}

- GET http://127.0.0.1:5000/products
- GET http://127.0.0.1:5000/products/1
- DELETE http://127.0.0.1:5000/products/1

---

## Author

Alhanoof Alabdullah
