'''
This file contains the callbacks for our Dash application.
'''
from app import app
from dash.dependencies import Input, Output, State
from models import Task
from database import db
# Add your callbacks here
@app.callback(
    Output('output-component', 'children'),
    [Input('submit-button', 'n_clicks')],
    state=[State('task-title', 'value'),
           State('task-description', 'value'),
           State('task-priority', 'value'),
           State('task-assignment', 'value'),
           State('task-ending-date', 'value')]
)
def create_task(n_clicks, title, description, priority, assignment, ending_date):
    if n_clicks is not None and title and description and priority and assignment and ending_date:
        new_task = Task(title=title, description=description, priority_level=priority, assignment=assignment, ending_date=ending_date)
        db.session.add(new_task)
        db.session.commit()
        return 'Task created successfully'
    return 'Please fill in all the task details'