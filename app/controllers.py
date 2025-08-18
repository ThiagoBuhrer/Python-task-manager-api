from flask import request, jsonify
from app.models import Task
from app import db


# -- Reusable Validations -- 

# Checks if data is 'None' or an empty dictionary ({})
def validate_task_exists(task):
    if not task:
        return jsonify({'error': 'Task not found. Please, insert a different task ID'}), 404
    return None


# -- Controller methods -- 

# POST (create new task)
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
def update_task(id):

     # Retrieves the task by its ID from database and validates its existence
    task = Task.query.get(id)
    validation = validate_task_exists(task)
    if validation:
        return validation

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

    # Returns a JSON response of sucessful update
    return jsonify({'message': 'Task updated successfully'}), 200

# DELETE (removes an existing task)
def delete_task(id):

    # Retrieves the task by its ID from database and validates its existence
    task = Task.query.get(id)
    validation = validate_task_exists(task)
    if validation:
        return validation

    db.session.delete(task)
    db.session.commit()

    # Returns a JSON response with the updated list of tasks
    return jsonify({'message': 'Task deleted successfully'}), 200
