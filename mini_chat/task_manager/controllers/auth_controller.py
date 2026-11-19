from flask import g, jsonify, request
import pymysql
from services.auth_service import register_user, login_user


class AuthController:
    @staticmethod
    def register():
        data = request.get_json(silent=True) or {}
        email = data.get("email")
        password = data.get("password")
        if not email or not password:
            return jsonify({"error": "email and password required"}), 400
        try:
            register_user(email, password)
        except pymysql.err.IntegrityError:
            return jsonify({"error": "email already used"}), 409
        return jsonify({"message": "created"}), 201

    @staticmethod
    def login():
        data = request.get_json(silent=True) or {}
        token = login_user(data.get("email"), data.get("password", ""))
        if token is None:
            return jsonify({"error": "invalid credentials"}),401
        return jsonify({"token": token})

    @staticmethod
    def me():
        return jsonify({"user_id": g.current_user["user_id"], "role": g.current_user["role"]})