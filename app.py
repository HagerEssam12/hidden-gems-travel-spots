from flask import Flask

# Import application blueprints
from routes.auth_routes import auth_bp
from routes.spot_routes import spot_bp

# Create the Flask application
app = Flask(__name__)

# Secret key used to manage user sessions
app.secret_key = "hidden-gems-secret-key"

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(spot_bp)

# Run the application
if __name__ == "__main__":
    app.run(debug=True)