# Refresh Token API

A professional Flask API project implementing access tokens and refresh tokens using JWT.

---

## Overview

This project demonstrates how to build a secure authentication flow using Flask with short-lived access tokens and refresh tokens.

---

## Features

- User registration
- User login
- Password hashing
- Access token generation
- Refresh token generation
- Token refresh endpoint
- Protected route access
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

### Refresh access token
POST /refresh

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

## Use the access token for protected routes:

Authorization: Bearer YOUR_ACCESS_TOKEN

## Use the refresh token in the refresh endpoint body:

{
  "refresh_token": "YOUR_REFRESH_TOKEN"
}


## Setup Commands

- cd ~/Flask-API-Projects
- mkdir project-14-refresh-token-api
- cd project-14-refresh-token-api
- touch README.md app.py requirements.txt

## Run the Project

- pip install -r requirements.txt
- python app.py

## Git Commands

- cd ..
- git add .
- git commit -m "add project 14 refresh token api"
- git push

## Testing with Postman

1) Health Check

GET http://127.0.0.1:5000/

2) Register

POST http://127.0.0.1:5000/register

{
  "username": "alhanoof",
  "password": "123456"
}

3) Login

POST http://127.0.0.1:5000/login

{
  "username": "alhanoof",
  "password": "123456"
}

4) Protected Route

GET http://127.0.0.1:5000/profile

## Header:

Authorization: Bearer YOUR_ACCESS_TOKEN

5) Refresh Access Token

{
  "refresh_token": "YOUR_REFRESH_TOKEN"
}

---------------------------
Author

Alhanoof Alabdullah
