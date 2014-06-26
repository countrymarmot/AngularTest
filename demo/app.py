from demo import app, db, manager
from models import Player
from flask import render_template
from flask.ext.babel import gettext as _


db.create_all()
manager.create_api(Player, methods=["GET", "POST", "DELETE"])


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
