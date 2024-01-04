from flask import Blueprint, render_template, request, jsonify
from app.models.users import User
from app.services.auth_service import AuthService

authbp = Blueprint("auth", __name__)

@authbp.route("/register", methods = ["Post", "Get"])
def register():
    if request.method == "POST":
        data = request.form
        try:
            new_user = AuthService.register_user(
                name=data["name"],
                username=data["username"],
                company=data["company"],
                email=data["email"],
                role=data["role"],
                password=data["password"]
            )
            return jsonify(message="User Registered Successfully"), 200
        except ValueError as e:
            return jsonify(error=str(e)), 400
    else:
        return render_template("register.html")

@authbp.route("/login", methods=["Post", "Get"])
def login():
    if request.method == "POST":
        data = request.form
        print(data)
        user = AuthService.authenticate_user(username=data["username"], password=data["password"])
        if user:
            return jsonify(message= "Login Successful"), 200
        elif user == None:
            return jsonify(message="User Not Registered"), 400
        else:
            return jsonify(message= "Wrong Password"), 400
    else:
        return render_template("login.html")