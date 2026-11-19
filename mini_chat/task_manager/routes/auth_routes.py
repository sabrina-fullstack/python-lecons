from flask import Blueprint
from controllers.auth_controller import AuthController

auth_bp = Blueprint("auth", __name__)

auth_bp.post("/register")(AuthController.register)
auth_bp.post("/login")(AuthController.login)
auth_bp.get("/me")(AuthController.me)