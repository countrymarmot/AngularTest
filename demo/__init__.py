from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager
from flask.ext.babel import Babel

app = Flask(__name__)
app.config.from_object("demo.settings")
db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)
babel = Babel(app)
