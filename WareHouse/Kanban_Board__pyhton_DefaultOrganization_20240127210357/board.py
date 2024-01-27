'''
This file defines the Board class which handles the logic for the Kanban board.
It allows tasks to be added to and moved between categories.
'''
import tkinter as tk
from category import Category
class Board:
    def __init__(self, root):
        self.root = root
        self.categories = ['Work', 'Personal', 'Repeatable']
        self.frames = {category: tk.Frame(self.root) for category in self.categories}
        self.category_objects = {category: Category(self.frames[category], category, self) for category in self.categories}
        for i, category in enumerate(self.categories):
            self.frames[category].grid(row=0, column=i)
            self.category_objects[category].show()
    def move_task(self, task, from_category, to_category):
        self.category_objects[from_category].remove_task(task)
        self.category_objects[to_category].add_task(task)