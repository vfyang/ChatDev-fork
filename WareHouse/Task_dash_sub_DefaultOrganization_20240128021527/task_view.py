'''
This file defines the Task view.
'''
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from models import Task
layout = html.Div([
    dcc.Input(id='task-input', type='text', placeholder='Enter a task'),
    html.Button('Submit', id='task-button', type='submit'),
    html.Div(id='task-output')
])
@app.callback(
    Output('task-output', 'children'),
    [Input('task-button', 'n_clicks')],
    [dash.dependencies.State('task-input', 'value')]
)
def update_output(n_clicks, value):
    if n_clicks is not None:
        task = Task(title=value)
        db.session.add(task)
        db.session.commit()
        return 'Task added: {}'.format(value)