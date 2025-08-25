from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    # Flask() constructor instantiates a new web application object
    # This object is responsible for handling all incoming HTTP requests
    app = Flask(__name__)

    # Load the configurations from Config class
    from config import Config
    app.config.from_object(Config)

    # Initialize db with app
    db.init_app(app)

    # Registers the 'main' blueprint in the main Flask application 
    from app.routes import main
    app.register_blueprint(main)

    return app
