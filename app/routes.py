from flask import Blueprint

# Blueprint lets us group routes (like modules)
# It handles them separately from the main application
main = Blueprint('main', __name__)

# Basic test route responding to GET requests
@main.route('/')
def hello():
    return "Hello, World!"
