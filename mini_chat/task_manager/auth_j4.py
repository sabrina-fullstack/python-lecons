import jwt
import pymysql
from datetime import datetime, timedelta, timezone
from werkzeug.security import generate_password_hash, check_password_hash

SECRET = "une-longue-cle-secrete-de-test-1234567890"


def get_conn():
    return pymysql.connect(
        host="localhost", port=3306, user="root",
        password="school123", database="task_manager",
        cursorclass=pymysql.cursors.DictCursor
    )


def register(email, password):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (email, password_hash) VALUES (%s, %s)",
        (email, generate_password_hash(password))
    )
    conn.commit()
    conn.close()


def login(email, password):
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


register("sabrina@test.com", "abc123")
print(login("sabrina@test.com", "abc123"))
print(login("sabrina@test.com", "wrong"))