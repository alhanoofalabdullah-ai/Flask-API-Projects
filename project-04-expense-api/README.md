# Expense API

A Flask API for tracking and analyzing expenses.

## Features
- Add expense
- View expenses
- Delete expense
- Search expenses
- Filter by category
- Calculate total spending
- Generate report by category

## Endpoints
- GET /expenses
- POST /expenses
- DELETE /expenses/<id>
- GET /expenses/search?q=name
- GET /expenses/filter?category=food
- GET /expenses/total
- GET /expenses/report

## Run
```bash
pip install flask
python app.py
