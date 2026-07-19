from flask import Blueprint, render_template, request, redirect, url_for, session
from logic.spot_logic import add_spot, load_spots, filter_spots
from logic.user_logic import add_favorite, remove_favorite, get_user_favorites
# Create a Blueprint for travel spot routes
spot_bp = Blueprint("spots", __name__)


# Display and filter travel spots on the home page
@spot_bp.route("/")
def home():
    # Redirect users who are not logged in
    if "username" not in session:
        return redirect(url_for("auth.login"))

    # Get search and category values from the URL
    search_query = request.args.get("search", "")
    category = request.args.get("category", "")

    # Load and filter travel spots
    spots = load_spots()
    spots = filter_spots(spots, search_query, category)

    return render_template(
        "home.html",
        spots=spots,
        search_query=search_query,
        selected_category=category,
        total_spots=len(spots)
    )

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

# Add a travel spot to favorites
@spot_bp.route("/favorite/<int:spot_id>")
def favorite_spot(spot_id):
    # Redirect users who are not logged in
    if "username" not in session:
        return redirect(url_for("auth.login"))

    # Add the spot to the logged-in user's favorites
    add_favorite(session["username"], spot_id)

    return redirect(url_for("spots.home"))

# Display the logged-in user's favorite travel spots
@spot_bp.route("/favorites")
def favorites():
    # Redirect users who are not logged in
    if "username" not in session:
        return redirect(url_for("auth.login"))

    # Get the user's favorite spot IDs
    favorite_ids = get_user_favorites(session["username"])

    # Load all travel spots
    spots = load_spots()

    # Keep only the user's favorite spots
    favorite_spots = [
        spot for spot in spots
        if spot["id"] in favorite_ids
    ]

    return render_template(
        "favorites.html",
        spots=favorite_spots
    )

# Remove a travel spot from favorites
@spot_bp.route("/remove-favorite/<int:spot_id>")
def remove_favorite_spot(spot_id):
    # Redirect users who are not logged in
    if "username" not in session:
        return redirect(url_for("auth.login"))

    # Remove the spot from the logged-in user's favorites
    remove_favorite(session["username"], spot_id)

    return redirect(url_for("spots.favorites"))