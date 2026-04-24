# Role-Based Access API

A professional Flask API project implementing user authentication and role-based access control using JWT.

---

## Overview

This project demonstrates how to build a secure Flask API with user registration, login, JWT authentication, and role-based authorization for protected routes.

---

## Features

- User registration
- User login
- Password hashing
- JWT token generation
- Protected routes
- Role-based access control
- Admin-only endpoint
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

### User profile
GET /profile

### Admin dashboard
GET /admin

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
## Register Request

{
  "username": "adminuser",
  "password": "123456",
  "role": "admin"
}

## Login Request

{
  "username": "adminuser",
  "password": "123456"
}

## Authentication

## After login, use the returned token in the request header:

Authorization: Bearer YOUR_TOKEN

## Roles

## Supported roles:

- admin
- user

## Setup Commands

- cd ~/Flask-API-Projects
- mkdir project-13-role-based-access-api
- cd project-13-role-based-access-api
- touch README.md app.py requirements.txt

## Run the Project

- pip install -r requirements.txt
- python app.py

## Git Commands

- cd ..
- git add .
- git commit -m "add project 13 role based access api"
- git push

## Testing with Postman

1) Health Check

GET http://127.0.0.1:5000/

2) Register Admin

POST http://127.0.0.1:5000/register

{
  "username": "adminuser",
  "password": "123456",
  "role": "admin"
}

3) Register Normal User

POST http://127.0.0.1:5000/register

{
  "username": "normaluser",
  "password": "123456",
  "role": "user"
}

4) Login

POST http://127.0.0.1:5000/login

{
  "username": "adminuser",
  "password": "123456"
}

5) Profile

GET http://127.0.0.1:5000/profile

## Header:

Authorization: Bearer YOUR_TOKEN

6) Admin Dashboard

GET http://127.0.0.1:5000/admin

## Header:

Authorization: Bearer YOUR_TOKEN


----------------
Author
Alhanoof Alabdullah
