from flask import Blueprint, request, jsonify
from app import db
from app.models import Task


# Blueprint named "main" lets us group routes (like modules)
# It handles them separately from the main application
main = Blueprint('main', __name__)


# Basic test route responding to GET requests
@main.route('/') # Decorator @ maps the '/' URL path to the following function
def hello():
    return "Hello, World!"


# POST (create new task)
@main.route('tasks', methods=['POST'])
def create_task():

    # Retrieves JSON data sent in the request body
    # Then converts it into a Python object (usually a dictionary)
    data = request.json

    if not data or 'title' not in data:
        return jsonify({'error': 'Title field is required.'}), 400

    # Creates a new instance of the Task class
    new_task = Task(
        title=data['title'],
        description=data.get('description'),
        status=data.get('status', 'pending')
    )

    # Adds the new task to the database session
    db.session.add(new_task)
    db.session.commit()

    # Returns a JSON response with the created task details
    # Sets the correct Content-Type: application/json header automatically
    return jsonify({
            'message': 'Tarefa criada com sucesso',
            'task': {
                'id': new_task.id,
                'title': new_task.title,
                'description': new_task.description,
                'status': new_task.status,
                'created_at': new_task.created_at
            }
        }), 201 # 201 status code indicates that a resource has been created successfully


# GET (retrieve all tasks)
@main.route('tasks', methods=['GET'])
def get_tasks():

    # Retrieves all records from the Task table in the database
    tasks = Task.query.all()

    # Store data in a dictionary (format suitable for returning as a JSON response)
    result = []

    # Iterates through each task and formats it for the response
    for task in tasks:
        result.append({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'created_at': task.created_at
        })

    # Returns a JSON response with the list of tasks
    # Sets the correct Content-Type: application/json header automatically
    return jsonify(result), 200


# PUT (update an existing task)
@main.route('tasks', methods=['PUT'])
def update_task(id):

    # Retrieves the task by its ID from the database
    task = Task.query.get(id)

    if not task:
        return jsonify({'error': 'Task not found. Please, insert a different task ID'}), 404
    
    # Retrieves JSON data sent in the request body
    # Then converts it into a Python object (usually a dictionary)
    data = request.json

    # Checks if data is 'None' or an empty dictionary ({})
    if not data:
        return jsonify({'error': 'Task not found.'}), 400
    
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.status = data.get('status', task.status)

    db.session.commit()


# DELETE (removes an existing task)
@main.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):

    # Retrieves the task by its ID from the database
    task = Task.query.get(id)
    
    if not task:
        return jsonify({'error': 'Task not found. Please, insert a different task ID'}), 404
    
    db.session.delete(task)
    db.session.commit()

    # Returns a JSON response with the updated list of tasks
    return jsonify({'message': 'Tarefa deletada com sucesso'}), 200
