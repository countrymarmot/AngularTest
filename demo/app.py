from demo import app, db, manager, babel
from models import Player
from flask import render_template
from flask import g, request
from flask.ext.babel import gettext as _


db.create_all()
manager.create_api(Player, methods=["GET", "POST", "DELETE"])


@babel.localeselector
def get_locale():
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    # otherwise try to guess the language from the user accept
    # header the browser transmits.
    return request.accept_languages.best_match(['zh_CN', 'en', 'en_us'])


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
