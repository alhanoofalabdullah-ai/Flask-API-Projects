# JWT Authentication API

A professional Flask API project for user registration, login, and protected routes using JWT authentication.

---

## Overview

This project demonstrates how to build a secure authentication API using Flask, SQLite, password hashing, and JWT tokens.

---

## Features

- User registration
- User login
- Password hashing
- JWT token generation
- Protected route access
- Token-based authentication
- SQLite database integration
- Input validation
- JSON responses

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- database.db → SQLite database
- README.md → Project documentation

---

## Endpoints

### Register user
POST /register

### Login user
POST /login

### Protected route
GET /profile

---

## Technologies Used

- Python
- Flask
- SQLite
- JWT
- Werkzeug
- REST API

---

## Run the Project

```bash
pip install -r requirements.txt
python app.py

## Example JSON
## Register / Login Request

{
  "username": "alhanoof",
  "password": "123456"
}

## Authentication

## After login, use the returned token in the request header:

- Authorization: Bearer YOUR_TOKEN

## Setup Commands

- cd ~/Flask-API-Projects
- mkdir project-12-jwt-authentication-api
- cd project-12-jwt-authentication-api
- touch README.md app.py requirements.txt

## Run the Project

- pip install -r requirements.txt
python app.py

## Git Commands

- cd ..
- git add .
- git commit -m "add project 12 jwt authentication api"
- git push

## Testing with Postman

1) Health Check

GET http://127.0.0.1:5000/

2) Register

POST http://127.0.0.1:5000/register

## Request body:

{
  "username": "alhanoof",
  "password": "123456"
}

3) Login

POST http://127.0.0.1:5000/login

## Request body:

{
  "username": "alhanoof",
  "password": "123456"
}

4) Protected Route

## Header:

Authorization: Bearer YOUR_TOKEN

---------------
Author

Alhanoof Alabdullah
