from flask import Blueprint, render_template, request, redirect, url_for, session
from logic.spot_logic import add_spot, load_spots

# Create a Blueprint for travel spot routes
spot_bp = Blueprint("spots", __name__)


# Display all travel spots on the home page
@spot_bp.route("/")
def home():
    # Redirect users who are not logged in
    if "username" not in session:
        return redirect(url_for("auth.login"))

    # Load all travel spots
    spots = load_spots()

    return render_template("home.html", spots=spots)


# Handle adding a new travel spot
@spot_bp.route("/add-spot", methods=["GET", "POST"])
def add_new_spot():
    # Redirect users who are not logged in
    if "username" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        location = request.form["location"]
        category = request.form["category"]
        image_url = request.form["image_url"]

        # Add the new spot using the logged-in username
        add_spot(
            name,
            description,
            location,
            category,
            image_url,
            session["username"]
        )

        return redirect(url_for("spots.home"))

    return render_template("add_spot.html")