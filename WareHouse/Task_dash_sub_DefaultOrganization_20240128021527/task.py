'''
This file defines the Task model.
'''
from app import db
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))
    priority_level = db.Column(db.Integer, nullable=False)
    assignment = db.Column(db.String(80), nullable=False)
    ending_date = db.Column(db.DateTime, nullable=False)