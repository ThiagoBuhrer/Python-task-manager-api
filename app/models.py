from app import db
from datetime import datetime, timezone

# Defines the data model for 'tasks' in the database
class Task (db.Model):
    id = db.Column(db.Integer, primary_key=True)                    
    title = db.Column(db.String(100), nullable=False)             
    description = db.Column(db.Text, nullable=True)                 
    status = db.Column(db.String(20), default='pending')            
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))   
    
    def __repr__(self):
        # Provides a developer-friendly string representation for debugging
        return f'<Task {self.id} - {self.title}>'
    