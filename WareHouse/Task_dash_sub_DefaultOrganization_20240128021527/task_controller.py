'''
This file defines the Task controller.
'''
from app import db
from app.models import Task
def create_task(title, description, priority_level, assignment, ending_date):
    task = Task(title=title, description=description, priority_level=priority_level, assignment=assignment, ending_date=ending_date)
    db.session.add(task)
    db.session.commit()