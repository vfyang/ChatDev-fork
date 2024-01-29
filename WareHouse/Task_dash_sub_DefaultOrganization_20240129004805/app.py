'''
This file contains the Dash application and the layout of our website.
'''
import dash
import dash_bootstrap_components as dbc
from dash import html
from database import db
from models import Task, User
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    html.H1('Task Management System', style={'color': 'blue'}),
    dbc.Input(id='task-title', placeholder='Enter task title', type='text'),
    dbc.Input(id='task-description', placeholder='Enter task description', type='text'),
    dbc.Input(id='task-priority', placeholder='Enter task priority', type='number'),
    dbc.Input(id='task-assignment', placeholder='Enter task assignment', type='text'),
    dbc.Input(id='task-ending-date', placeholder='Enter task ending date', type='date'),
    dbc.Button('Submit', id='submit-button', color='primary'),
    # Add more components as needed
])
server = app.server