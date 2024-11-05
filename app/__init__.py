from flask import Flask
from .db import db, migrate
from .models import book
import os
from .routes.book_routes import bp as books_bp


def create_app(config=None):
    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development"
    )

    if config:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(books_bp)

    return app
    # app.register_blueprint(hello_world_bp)
