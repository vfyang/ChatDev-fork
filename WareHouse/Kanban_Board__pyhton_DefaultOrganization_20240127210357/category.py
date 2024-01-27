'''
This file defines the Category class which handles the logic for each category in the Kanban board.
It allows tasks to be added and moved.
'''
import tkinter as tk
class Category:
    def __init__(self, frame, name, board):
        self.frame = frame
        self.name = name
        self.board = board
        self.tasks = []
        self.entry = tk.Entry(self.frame)
        self.entry.pack()
        self.button = tk.Button(self.frame, text="Add task", command=self.add_task_from_entry)
        self.button.pack()
    def show(self):
        label = tk.Label(self.frame, text=self.name)
        label.pack()
        self.show_tasks()
    def add_task(self, task):
        self.tasks.append(task)
        self.show_tasks()
    def remove_task(self, task):
        self.tasks.remove(task)
        self.show_tasks()
    def add_task_from_entry(self):
        task = self.entry.get()
        self.add_task(task)
    def show_tasks(self):
        for widget in self.frame.winfo_children():
            if not isinstance(widget, (tk.Entry, tk.Button)):
                widget.destroy()
        for task in self.tasks:
            label = tk.Label(self.frame, text=task)
            label.pack()
            dropdown = tk.OptionMenu(self.frame, tk.StringVar(), *self.board.categories, command=lambda new_category: self.board.move_task(task, self.name, new_category))
            dropdown.pack()