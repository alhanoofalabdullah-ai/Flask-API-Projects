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

---------------------------
Author

Alhanoof Alabdullah
