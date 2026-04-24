from flask import Flask, jsonify

app = Flask(__name__)


def success_response(message, data=None, status_code=200):
    response = {
        "success": True,
        "message": message
    }

    if data is not None:
        response["data"] = data

    return jsonify(response), status_code


@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    return response


@app.route("/", methods=["GET"])
def home():
    return success_response("API Security Headers Pro is running")


@app.route("/secure-data", methods=["GET"])
def secure_data():
    data = {
        "security": "enabled",
        "headers": [
            "X-Content-Type-Options",
            "X-Frame-Options",
            "Content-Security-Policy",
            "Referrer-Policy",
            "Permissions-Policy"
        ]
    }

    return success_response("Secure data retrieved successfully", data)


if __name__ == "__main__":
    app.run(debug=True)
