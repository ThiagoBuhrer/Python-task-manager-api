from app import db
from app.models import Task


# --- RESET DATABASE (optional, for testing only) ---
db.drop_all() # Drops all tables
db.create_all() # Creates all tables again


# --- Test CREATE (add tasks) ---
# Note: not adding a status will automaticallt set it to 'pending'
task1 = Task(title="Grocery shopping", description="Buy fruits, vegetables, and other essentials")
task2 = Task(title="Clean the house", description="Vacuum, dust, and organize rooms")
task3 = Task(title="Daily exercise", description="Go for a run or do a home workout", status="completed")
task4 = Task(title="Cook dinner", description="Prepare a healthy meal for the evening", status="completed")
task5 = Task(title="Water the plants", description="Water all indoor and outdoor plants", status="completed")


db.session.add_all([task1, task2, task3, task4, task5])  
db.session.commit()


# --- Test READ (get all tasks) ---
tasks = Task.query.all()
print("Tasks in database:")
for task in tasks:
    print(task.id, task.title, task.status)


# --- Test UPDATE (modify existing tasks) ---
tasks = Task.query.all() # Retrieves all tasks and store them in a list

task_to_update = tasks[2] # Chooses the third task 
task_to_update.status = "pending"
db.session.commit()
task_to_update = tasks[0] # Chooses the first task
task_to_update.description = "Wash the sink, clean the toilets, broom the floor"
db.session.commit()


# --- Test DELETE (remove tasks) ---
task_to_delete = Task.query.filter_by(title="Water the plants").first()
if task_to_delete:
    db.session.delete(task_to_delete)
    db.session.commit()
    print(f"Task deleted: {task_to_delete.id} - {task_to_delete.title}")
else:
    print("Task not found.")
