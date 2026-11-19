import os
import jwt
from datetime import datetime, timedelta, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from config.db import get_conn
SECRET = os.getenv("JWT_SECRET")


def register_user(email, password):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (email, password_hash) VALUES (%s, %s)",
        (email, generate_password_hash(password))
    )
    conn.commit()
    conn.close()


def login_user(email, password):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    conn.close()
    if user is None or not check_password_hash(user["password_hash"], password):
        return None
    payload = {
        "user_id": user["id"],
        "role": user["role"],
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")
def decode_token(token):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except jwt.____:
        return None