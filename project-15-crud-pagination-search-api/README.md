# CRUD API with Pagination and Search

A professional Flask API project implementing CRUD operations with pagination and search functionality.

---

## Overview

This project demonstrates how to build a RESTful API using Flask with item creation, retrieval, update, deletion, pagination, and search.

---

## Features

- Create items
- Get all items
- Get item by ID
- Update items
- Delete items
- Search by item name
- Pagination support
- SQLite database integration
- JSON responses

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

### Create Item
POST /items

### Get Items with Pagination and Search
GET /items?page=1&limit=5&search=laptop

### Get Item by ID
GET /items/<id>

### Update Item
PUT /items/<id>

### Delete Item
DELETE /items/<id>

---

## Technologies Used

- Python
- Flask
- SQLite
- REST API
- Pagination
- Search

## Setup Commands

- cd ~/Flask-API-Projects
- mkdir project-15-crud-pagination-search-api
- cd project-15-crud-pagination-search-api
- touch README.md app.py requirements.txt

## Run the Project

- pip install -r requirements.txt
- python app.py

## Git Commands

- cd ..
- git add .
- git commit -m "add project 15 crud pagination search api"
- git push

## Testing Examples

- GET http://127.0.0.1:5000/
- POST http://127.0.0.1:5000/items

{
  "name": "Laptop",
  "category": "Electronics",
  "price": 3500
}

- GET http://127.0.0.1:5000/items?page=1&limit=5
- GET http://127.0.0.1:5000/items?search=laptop
- GET http://127.0.0.1:5000/items/1
- PUT http://127.0.0.1:5000/items/1

{
  "name": "Gaming Laptop",
  "category": "Electronics",
  "price": 4500
}

- DELETE http://127.0.0.1:5000/items/1

---

## Author

Alhanoof Alabdullah
