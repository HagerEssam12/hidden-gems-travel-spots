from flask import Blueprint, render_template, request, redirect, url_for, session
from logic.user_logic import user_exists, add_user, validate_user

# Create a Blueprint for authentication routes
auth_bp = Blueprint("auth", __name__)

# Handle user registration
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Check if the username already exists
        if user_exists(username):
            return "Username already exists"

        # Add the new user
        add_user(username, password)

        return redirect(url_for("auth.login"))

    return render_template("register.html")

# Handle user login
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Store the logged-in username in the session
        if validate_user(username, password):
            session["username"] = username
            return "Login successful"

        return "Invalid username or password"

    return render_template("login.html")

# Handle user logout
@auth_bp.route("/logout")
def logout():
    # Remove the username from the session
    session.pop("username", None)

    return redirect(url_for("auth.login"))