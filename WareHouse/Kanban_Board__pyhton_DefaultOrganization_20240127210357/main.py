'''
This is the main file for the Kanban board application. 
It sets up the GUI and handles user interactions.
'''
import tkinter as tk
from board import Board
class KanbanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kanban Board")
        self.board = Board(self.root)
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    app = KanbanApp(root)
    app.run()