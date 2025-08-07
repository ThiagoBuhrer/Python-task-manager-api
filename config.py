import os

# Get the absolute path of this file's directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# class Config serves as the central place to define app's settings
class Config:

    # Database connection string
    # (address used by Flask/SQLAlchemy to find the database)
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'tasks.db')}"

    # Disables change tracking to save resource
    SQLALCHEMY_TRACK_MODIFICATIONS = False