'''
This is the main file that runs the application.
'''
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app, server
from views import task_view, user_view
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/tasks':
        return task_view.layout
    elif pathname == '/users':
        return user_view.layout
    else:
        return '404'
if __name__ == "__main__":
    app.run_server(debug=True)