from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.routes import main

# Flask() constructor instantiates a new web application object
# This object is responsible for handling all incoming HTTP requests
app = Flask(__name__)

# Load the configurations from Config class
app.config.from_object(Config)

# Connects Flask with SQLAlchemy using Flask's configurations
db = SQLAlchemy(app)

# Registers the 'main' blueprint in the main Flask application 
app.register_blueprint(main)
