import jwt
from datetime import datetime, timedelta, timezone

SECRET = "test-secret"

payload = {
    "user_id": 1,
    "role": "admin",
    "exp": datetime.now(timezone.utc) + timedelta(hours=1)
}

token = jwt.encode(payload, SECRET, algorithm="HS256")
print(token)

data = jwt.decode(token, SECRET, algorithms=["HS256"])
print(data["user_id"], data["role"])