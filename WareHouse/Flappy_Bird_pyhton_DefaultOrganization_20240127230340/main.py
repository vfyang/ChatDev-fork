'''
This is the main file that will run the game. It imports the necessary classes and starts the game loop.
'''
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from game import Game
app = dash.Dash(__name__)
# Create the game object outside the callback
game = Game()
app.layout = html.Div([
    dcc.Graph(id='live-update-graph'),
    html.Button('Jump', id='jump-button', n_clicks=0),
    dcc.Interval(
        id='interval-component',
        interval=1*1000, # in milliseconds
        n_intervals=0
    )
])
@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals'), Input('jump-button', 'n_clicks')])
def update_graph_live(n, n_clicks):
    # Update the game object
    game.update(n_clicks)
    return game.draw()
if __name__ == '__main__':
    app.run_server(debug=True)