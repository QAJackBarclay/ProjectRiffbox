from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pdb

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

from application import routes

