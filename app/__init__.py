from flask import Flask
from .routes import routes

def create_app():
    app = Flask(__name__)

    # Register the routes blueprint
    app.register_blueprint(routes)

    return app
