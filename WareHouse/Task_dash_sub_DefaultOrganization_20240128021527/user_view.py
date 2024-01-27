'''
This file defines the User view.
'''
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from models import User
layout = html.Div([
    dcc.Input(id='user-input', type='text', placeholder='Enter a username'),
    html.Button('Submit', id='user-button', type='submit'),
    html.Div(id='user-output')
])
@app.callback(
    Output('user-output', 'children'),
    [Input('user-button', 'n_clicks')],
    [dash.dependencies.State('user-input', 'value')]
)
def update_output(n_clicks, value):
    if n_clicks is not None:
        user = User(username=value)
        db.session.add(user)
        db.session.commit()
        return 'User added: {}'.format(value)