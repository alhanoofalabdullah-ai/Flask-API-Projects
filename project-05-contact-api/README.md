# Contact API

A Flask API for managing contacts.

## Features
- Add contact
- View contacts
- Update contact
- Delete contact
- Search by name
- Filter by email

## Endpoints
- GET /contacts
- POST /contacts
- PUT /contacts/<id>
- DELETE /contacts/<id>
- GET /contacts/search?q=name
- GET /contacts/filter?email=gmail

## Run
```bash
pip install flask
python app.py
