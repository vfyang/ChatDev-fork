'''
This file initializes the Dash application and the database.
'''
import dash
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(server)
app = dash.Dash(__name__, server=server)
from models import Task, User