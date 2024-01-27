manual.md

```
# Python Kanban Board

A simple, intuitive, and interactive Kanban board application developed in Python. It allows you to manage and organize your tasks into different categories - 'Work', 'Personal', and 'Repeatable'.

## Quick Install

Before running the application, make sure you have Python installed on your system. If not, you can download it from [here](https://www.python.org/downloads/).

Next, install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## 🤔 What is this?

This is a Kanban board application developed in Python using the tkinter library for the GUI. It allows you to add tasks to different categories and move them between categories as needed. The categories available are 'Work', 'Personal', and 'Repeatable'.

## Main Features

- **Add Tasks:** You can add tasks to any category by typing the task in the text box and clicking the 'Add task' button.
- **Move Tasks:** You can move tasks between categories using the dropdown menu next to each task.
- **Delete Tasks:** Tasks are automatically deleted from a category when they are moved to another category.

## 📖 How to Use

1. Run the main.py file to start the application:

```bash
python main.py
```

2. The application window will open with three columns representing the categories 'Work', 'Personal', and 'Repeatable'.

3. To add a task, type the task in the text box at the top of the relevant category and click the 'Add task' button. The task will appear in the category column.

4. To move a task, click the dropdown menu next to the task and select the category you want to move the task to. The task will be removed from the current category and added to the selected category.

5. To close the application, simply close the application window.

## 📚 Documentation

For more detailed information on the application's structure and functionality, please refer to the comments in the code files:

- main.py: This file sets up the GUI and handles user interactions.
- board.py: This file handles the logic for the Kanban board, allowing tasks to be added to and moved between categories.
- category.py: This file handles the logic for each category, allowing tasks to be added and moved.

```