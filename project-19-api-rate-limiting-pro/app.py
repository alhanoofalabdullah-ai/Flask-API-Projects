import time
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

RATE_LIMIT = 5
TIME_WINDOW = 60

request_records = {}


def success_response(message, data=None, status_code=200):
    response = {
        "success": True,
        "message": message
    }

    if data is not None:
        response["data"] = data

    return jsonify(response), status_code


def error_response(message, status_code):
    return jsonify({
        "success": False,
        "error": {
            "message": message,
            "status_code": status_code
        }
    }), status_code


def rate_limit(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        client_ip = request.remote_addr
        current_time = time.time()

        if client_ip not in request_records:
            request_records[client_ip] = []

        request_records[client_ip] = [
            timestamp for timestamp in request_records[client_ip]
            if current_time - timestamp < TIME_WINDOW
        ]

        if len(request_records[client_ip]) >= RATE_LIMIT:
            return error_response(
                "Rate limit exceeded. Please try again later.",
                429
            )

        request_records[client_ip].append(current_time)

        return func(*args, **kwargs)

    return decorated


@app.route("/", methods=["GET"])
def home():
    return success_response("API Rate Limiting Pro is running")


@app.route("/data", methods=["GET"])
@rate_limit
def get_data():
    data = {
        "items": [
            {"id": 1, "name": "Laptop"},
            {"id": 2, "name": "Phone"},
            {"id": 3, "name": "Headphones"}
        ],
        "rate_limit": f"{RATE_LIMIT} requests per {TIME_WINDOW} seconds"
    }

    return success_response("Data retrieved successfully", data)


if __name__ == "__main__":
    app.run(debug=True)
