# Checklist Management System

This is a Python-based web application for managing checklists with an integrated user and task management system. The application allows users to create, manage, and track tasks with various attributes such as Title, Description, Priority Level, Assignment, and Ending Date. The application uses Bootstrap and Vue.js for the front-end and Dash for the back-end.

## Quick Install

Before you begin, make sure you have Python installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

Next, you need to install the necessary Python libraries. You can do this by running the following command in your terminal:

```bash
pip install dash dash-bootstrap-components pandas
```

## How to Use

1. **Start the Application**: Navigate to the directory where the application files are located and run the `main.py` file. This will start the application.

```bash
python main.py
```

2. **Access the Application**: Open a web browser and go to `http://localhost:8050`. This will take you to the application's home page.

3. **Create a User**: To create a new user, enter a username and email in the 'Add User' section and click the 'Submit' button.

4. **Create a Task**: To create a new task, enter the task details in the 'Add Task' section and click the 'Submit' button. The task details include Title, Description, Priority Level, Assignment, and Ending Date.

5. **View Tasks and Users**: The tasks and users you create will be displayed in the 'Tasks' and 'Users' sections respectively.

## Folder Structure

The application follows a standard Python project structure. Here is a brief overview of the main folders and files:

- `main.py`: This is the main file that runs the application.
- `app`: This directory contains the Flask application and the database initialization.
- `models`: This directory contains the Task and User models.
- `views`: This directory contains the Task and User views.
- `controllers`: This directory contains the Task and User controllers.
- `static`: This directory contains static files such as CSS and JavaScript files.
- `templates`: This directory contains HTML templates.

## Customization

You can customize the application to suit your needs. For example, you can change the color theme by modifying the CSS in the `index.html` file. You can also add new features or modify existing ones by editing the Python, HTML, and JavaScript files.

## Support

If you encounter any issues or need further assistance, feel free to reach out to us. We're here to help!