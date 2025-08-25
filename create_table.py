from app import create_app, db
from app.models import Task

# Creates the Flask application instance
app = create_app()

# Context manager "with" safely opens and closes resources automatically
with app.app_context():
    # Creates all database tables based on the defined models
    db.create_all()
    print("Database tables created successfully!")