import os
from dotenv import load_dotenv

load_dotenv()

from flask import Flask, g, jsonify, request
from routes.auth_routes import auth_bp
from services.auth_service import decode_token

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/api")

PUBLIC_ROUTES = ["/api/login", "/api/register"]


@app.before_request
def check_token():
    if request.path in PUBLIC_ROUTES:
        return None
    header = request.headers.get("Authorization", "")
    if not header.startswith("Bearer "):
        return jsonify({"error": "token missing"}), 401
    token = header.split(" ")[1]
    user = decode_token(token)
    if user is None:
        return jsonify({"error": "invalid token"}), 401
    g.current_user = user


if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", "5003")), debug=True)