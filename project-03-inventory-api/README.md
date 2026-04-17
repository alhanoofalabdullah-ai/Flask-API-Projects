# Inventory API

A Flask API for managing products and stock.

## Features
- Add product
- Update product
- Delete product
- Search products
- Filter by stock
- Calculate total inventory value

## Endpoints
- GET /products
- POST /products
- PUT /products/<id>
- DELETE /products/<id>
- GET /products/search?q=name
- GET /products/filter?stock=low
- GET /products/value

## Run
```bash
pip install flask
python app.py
