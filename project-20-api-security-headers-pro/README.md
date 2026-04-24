# API Security Headers Pro

A professional Flask API project focused on improving API security by adding important HTTP security headers.

---

## Overview

This project demonstrates how to add security headers to Flask API responses to reduce common web security risks.

---

## Features

- Add security headers to all responses
- Protect against MIME sniffing
- Enable basic XSS protection
- Control iframe embedding
- Add content security policy
- Return structured JSON responses

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- README.md → Project documentation

---

## Endpoints

### Health Check
GET /

### Secure Data
GET /secure-data

---

## Technologies Used

- Python
- Flask
- REST API
- Security Headers
- HTTP Response Handling

## Setup Commands

- cd ~/Flask-API-Projects
- mkdir project-20-api-security-headers-pro
- cd project-20-api-security-headers-pro
- touch README.md app.py requirements.txt

## Run

- pip install -r requirements.txt
- python app.py

## Git Commands

- cd ..
- git add .
- git commit -m "add project 20 api security headers pro"
- git push

## Testing Examples

- GET http://127.0.0.1:5000/
- GET http://127.0.0.1:5000/secure-data

---

## Author

Alhanoof Alabdullah
