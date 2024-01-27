'''
This file defines the User controller.
'''
from app import db
from app.models import User
def create_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()