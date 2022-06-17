from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pdb
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

from application import routes
