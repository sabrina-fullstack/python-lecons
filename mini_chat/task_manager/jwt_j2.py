from werkzeug.security import generate_password_hash, check_password_hash

password = "abc123"
hashed = generate_password_hash(password)
print(hashed)

print(check_password_hash(hashed, "abc123"))
print(check_password_hash(hashed, "wrong"))
