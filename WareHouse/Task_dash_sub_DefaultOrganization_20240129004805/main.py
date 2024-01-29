'''
This is the entry point of our application.
'''
from app import app
from database import db
if __name__ == "__main__":
    db.create_all()
    app.run_server(debug=True)