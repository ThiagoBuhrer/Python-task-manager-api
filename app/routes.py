from flask import Blueprint, request, jsonify
from app.controllers import create_task, get_tasks, update_task, delete_task


# Blueprint named "main" lets us group routes (like modules)
# It handles them separately from the main application
main = Blueprint('main', __name__)


# Basic test route responding to GET requests
@main.route('/') # Decorator @ maps the '/' URL path to the following function
def hello():
    return "Hello, World!"

# POST (create new task)
@main.route('/tasks', methods=['POST'])
def route_create_task():
    return create_task()

# GET (retrieve all tasks)
@main.route('/tasks', methods=['GET'])
def route_get_tasks():
    return get_tasks()

# PUT (update an existing task)
@main.route('/tasks/<int:id>', methods=['PUT'])
def route_update_task(id):
    return update_task(id)

# DELETE (removes an existing task)
@main.route('/tasks/<int:id>', methods=['DELETE'])
def route_delete_task(id):
    return delete_task(id)
