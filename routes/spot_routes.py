from flask import Blueprint, render_template, request, redirect, url_for, session

from logic.spot_logic import (
    add_spot,
    load_spots,
    filter_spots,
    delete_spot,
    get_spot_by_id,
    edit_spot
)

from logic.user_logic import (
    add_favorite,
    remove_favorite,
    get_user_favorites
)

# Create a Blueprint for all travel spot routes
spot_bp = Blueprint("spots", __name__)


# =========================
# Home Page
# =========================
@spot_bp.route("/")
def home():

    # Redirect users who are not logged in
    if "username" not in session:
        return redirect(url_for("auth.login"))

    # Get search and filter values
    search_query = request.args.get("search", "")
    category = request.args.get("category", "")

    # Load and filter travel spots
    spots = load_spots()
    spots = filter_spots(spots, search_query, category)

    # Get the logged-in user's favorite spots
    favorite_ids = get_user_favorites(session["username"])

    return render_template(
        "home.html",
        spots=spots,
        search_query=search_query,
        selected_category=category,
        total_spots=len(spots),
        favorite_ids=favorite_ids,
        favorite_count=len(favorite_ids)
    )


# =========================
# Add New Travel Spot
# =========================
@spot_bp.route("/add-spot", methods=["GET", "POST"])
def add_new_spot():

    # Redirect users who are not logged in
    if "username" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        add_spot(
            request.form["name"],
            request.form["description"],
            request.form["location"],
            request.form["category"],
            request.form["image_url"],
            session["username"]
        )

        return redirect(url_for("spots.home"))

    return render_template("add_spot.html")


# =========================
# Add / Remove Favorite
# =========================
@spot_bp.route("/favorite/<int:spot_id>")
def favorite_spot(spot_id):

    # Redirect users who are not logged in
    if "username" not in session:
        return redirect(url_for("auth.login"))

    favorite_ids = get_user_favorites(session["username"])

    # Toggle favorite status
    if spot_id in favorite_ids:
        remove_favorite(session["username"], spot_id)
    else:
        add_favorite(session["username"], spot_id)

    return redirect(url_for("spots.home"))


# =========================
# Favorites Page
# =========================
@spot_bp.route("/favorites")
def favorites():

    # Redirect users who are not logged in
    if "username" not in session:
        return redirect(url_for("auth.login"))

    favorite_ids = get_user_favorites(session["username"])

    spots = load_spots()

    # Keep only favorite travel spots
    favorite_spots = [
        spot
        for spot in spots
        if spot["id"] in favorite_ids
    ]

    return render_template(
        "favorites.html",
        spots=favorite_spots
    )


# =========================
# Delete Travel Spot
# =========================
@spot_bp.route("/delete/<int:spot_id>")
def delete_spot_route(spot_id):

    # Redirect users who are not logged in
    if "username" not in session:
        return redirect(url_for("auth.login"))

    spot = get_spot_by_id(spot_id)

    if not spot:
        return "Spot not found"

    # Only the owner can delete the travel spot
    if spot["added_by"] != session["username"]:
        return "You are not allowed to delete this spot."

    delete_spot(spot_id)

    return redirect(url_for("spots.home"))


# =========================
# Edit Travel Spot
# =========================
@spot_bp.route("/edit/<int:spot_id>", methods=["GET", "POST"])
def edit_spot_route(spot_id):

    # Redirect users who are not logged in
    if "username" not in session:
        return redirect(url_for("auth.login"))

    spot = get_spot_by_id(spot_id)

    if not spot:
        return "Spot not found"

    # Only the owner can edit the travel spot
    if spot["added_by"] != session["username"]:
        return "You are not allowed to edit this spot."

    if request.method == "POST":

        updated_data = {
            "name": request.form["name"],
            "description": request.form["description"],
            "location": request.form["location"],
            "category": request.form["category"],
            "image_url": request.form["image_url"]
        }

        edit_spot(spot_id, updated_data)

        return redirect(url_for("spots.home"))

    return render_template("edit_spot.html", spot=spot)