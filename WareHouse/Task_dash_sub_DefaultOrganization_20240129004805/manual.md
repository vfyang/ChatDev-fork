# Task Management System

This is a Dash-based Python web application for managing checklists with an integrated user and task management system. The application allows users to create tasks with a title, description, priority level, assignment, and ending date. The application uses Bootstrap for styling and Vue.js for the front-end framework.

## Quick Install

To install the necessary dependencies, run the following commands:

```bash
pip install dash
pip install dash-bootstrap-components
pip install flask_sqlalchemy
```

## Main Functionscd 

The main functions of the software include:

- **Task Creation:** Users can create tasks by entering the task title, description, priority level, assignment, and ending date. After entering all the details, users can click the 'Submit' button to create the task.

- **Task Management:** The application allows users to manage their tasks. Users can view all their tasks, edit the details of a task, or delete a task.

- **User Management:** The application also includes a user management system. Users can register for an account, log in to their account, and manage their account details.

## How to Use

To use the application, follow these steps:

1. **Start the Application:** Run the `main.py` script to start the application. This will create the database and start the server.

    ```bash
    python main.py
    ```

2. **Register for an Account:** Before you can create tasks, you need to register for an account. Click the 'Register' button and enter your username, email, and password.

3. **Log In:** After registering, you can log in to your account by clicking the 'Log In' button and entering your username and password.

4. **Create a Task:** To create a task, enter the task title, description, priority level, assignment, and ending date in the corresponding input fields. Then, click the 'Submit' button to create the task.

5. **Manage Tasks:** You can view all your tasks on the main page. To edit a task, click the 'Edit' button next to the task. To delete a task, click the 'Delete' button next to the task.

6. **Manage Account:** To manage your account details, click the 'Account' button. Here, you can change your username, email, or password.

## Folder Structure

The application has the following folder structure:

- `main.py`: This is the entry point of the application.
- `app.py`: This file contains the Dash application and the layout of the website.
- `callbacks.py`: This file contains the callbacks for the Dash application.
- `database.py`: This file contains the code for interacting with the database.
- `models.py`: This file contains the models for the tasks and users.

Make sure all these files are in the same directory and the folder structure is set up correctly.