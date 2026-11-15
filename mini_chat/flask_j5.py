import jwt
import pymysql
from datetime import datetime, timedelta, timezone
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

SECRET = "une-longue-cle-secrete-de-test-1234567890"

app = Flask(__name__)


def get_conn():
    return pymysql.connect(
        host="localhost", port=3306, user="root",
        password="school123", database="task_manager",
        cursorclass=pymysql.cursors.DictCursor
    )


@app.post("/register")
def register():
    data = request.get_json(silent=True) or {}
    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        return jsonify({"error": "email and password required"}), 400
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (email, password_hash) VALUES (%s, %s)",
            (email, generate_password_hash(password))
        )
        conn.commit()
    except pymysql.err.IntegrityError:
        return jsonify({"error": "email already used"}), 409
    finally:
        conn.close()
    return jsonify({"message": "created"}), 201


@app.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (data.get("email"),))
    user = cursor.fetchone()
    conn.close()
    if user is None or not check_password_hash(user["password_hash"], data.get("password", "")):
        return jsonify({"error": "invalid credentials"}), 401
    payload = {
        "user_id": user["id"],
        "role": user["role"],
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET, algorithm="HS256")
    return jsonify({"token": token})


@app.get("/me")
def me():
    header = request.headers.get("Authorization", "")
    if not header.startswith("Bearer "):
        return jsonify({"error": "token missing"}), 401
    token = header.split(" ")[1]
    try:
        data = jwt.decode(token, SECRET, algorithms=["HS256"])
    except jwt.InvalidTokenError:
        return jsonify({"error": "invalid token"}), 401
    return jsonify({"user_id": data["user_id"], "role": data["role"]})


if __name__ == "__main__":
    app.run(port=5003, debug=True)