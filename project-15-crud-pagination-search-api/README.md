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

---

## Author

Alhanoof Alabdullah
