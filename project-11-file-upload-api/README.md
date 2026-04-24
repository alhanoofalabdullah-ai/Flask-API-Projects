# File Upload API

A Flask API project for uploading files and storing them on the server.

---

## Overview

This project demonstrates how to build a simple file upload API using Flask. It allows users to upload files through an API endpoint and saves them in a local uploads folder.

---

## Features

- Upload files using API
- Save files locally
- Validate file input
- Return JSON responses
- Handle missing file errors

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- uploads/ → Uploaded files
- README.md → Project documentation

---

## Endpoints

### Upload file
POST /upload

### Health check
GET /

---

## Technologies Used

- Python
- Flask
- REST API
- File Handling

---

## Run the Project

```bash
pip install -r requirements.txt
python app.py

## Example Usage
## Health check

- GET http://127.0.0.1:5000/

## Upload file

- POST http://127.0.0.1:5000/upload

## Use form-data in Postman with:

- key: file
- type: File

## Setup Commands

- cd ~/Flask-API-Projects
- mkdir project-11-file-upload-api
- cd project-11-file-upload-api
- mkdir uploads
- touch README.md app.py requirements.txt

## Git Commands

- cd ..
- git add .
- git commit -m "add project 11 file upload api"
- git push

## Run the Project

- pip install -r requirements.txt
- python app.py

## Testing with Postman
## Health Check

- GET http://127.0.0.1:5000/

## Upload File

- POST http://127.0.0.1:5000/upload

## Request Body (Postman)

- Type: form-data
- Key: file
- Value Type: File

## Expected Response

{
  "message": "File uploaded successfully",
  "filename": "example.txt",
  "path": "uploads/example.txt"
}

-----------
Author

Alhanoof Alabdullah
