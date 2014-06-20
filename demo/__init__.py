from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

app = Flask(__name__, static_url_path="")
app.config.from_object("demo.settings")
db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)
