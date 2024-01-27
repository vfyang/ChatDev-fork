'''
This is the game module that contains the Game class. The Game class contains the logic for the game, including the bird's movement, collision detection, scoring, and drawing the game state.
'''
import plotly.graph_objects as go
class Game:
    def __init__(self):
        # Initialize game state
        self.bird_position = 0
        self.obstacle_position = 10
        self.score = 0
        self.jump = 0
    def update(self, jump):
        # Update game state (bird's movement, collision detection, scoring)
        self.bird_position += 1 if jump > self.jump else -1
        self.jump = jump
        self.obstacle_position -= 1
        if self.obstacle_position < 0:
            self.obstacle_position = 10
            self.score += 1
        if self.bird_position == self.obstacle_position:
            self.bird_position = 0
            self.score -= 1
    def draw(self):
        # Draw the current game state and return the figure
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[self.bird_position], y=[0], mode='markers', name='bird'))
        fig.add_trace(go.Scatter(x=[self.obstacle_position], y=[0], mode='markers', name='obstacle'))
        fig.update_layout(title_text="Score: {}".format(self.score))
        return fig