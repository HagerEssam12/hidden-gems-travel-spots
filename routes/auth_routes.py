from flask import Blueprint, render_template, request, redirect, url_for, session
from logic.user_logic import user_exists, add_user, validate_user

# Create a Blueprint for all authentication routes
auth_bp = Blueprint("auth", __name__)


# Register a new user
@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    error = None

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # Check if the username already exists
        if user_exists(username):
            error = "Username already exists."

        else:
            # Save the new user
            add_user(username, password)

            # Redirect the user to the login page
            return redirect(url_for("auth.login"))

    return render_template("register.html", error=error)

# Log in an existing user
@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    error = None

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # Validate the entered username and password
        if validate_user(username, password):

            # Store the logged-in username in the session
            session["username"] = username

            # Redirect to the home page
            return redirect(url_for("spots.home"))

        # Show error on the same page
        error = "Invalid username or password."

    return render_template("login.html", error=error)


# Log out the current user
@auth_bp.route("/logout")
def logout():

    # Remove the username from the current session
    session.pop("username", None)

    # Redirect back to the login page
    return redirect(url_for("auth.login"))