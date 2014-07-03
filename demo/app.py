from demo import app, db, babel
from models import Player, User
from flask import render_template
from flask import g, request, jsonify
from flask.ext.babel import gettext as _


db.create_all()
#manager.create_api(Player, methods=["GET", "POST", "DELETE"])


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'GET'):
        return render_template('login.html')
    elif(request.method == 'POST'):
        username = request.json.get('username')
        password = request.json.get('password')
        otp = request.json.get('otp')
        try:
            otp = int(otp)
        except ValueError:
            return _("invliad format of one time password. must be integer.")
        user = User.query.filter_by(name=username).first()
        if(user is None):
            return _("invalid user name.")
        elif(not user.verify_password(password)):
            return _("invalid passowrd.")
        elif(not user.authenticate(otp)):
            return _("invalid one time password.")
        else:
            g.user = user
            return "welcome, " + user.name


@app.route('/signup')
def signup():
    return render_template('register.html')


@app.route('/api/users', methods=['GET', 'POST'])
def userapi():
    if(request.method == 'GET'):
        return "unauthorized."  #todo
    elif(request.method == 'POST'):
        if(not validate_user(request.json)):
            return "not valid request."
        username = request.json.get('username')
        department = request.json.get('department')
        if(User.query.filter_by(name = username).first() is not None):
            return "user already exists."
        user = User(name=username, department=department)
        user.hash_password(request.json.get('password'))
        otpauth = user.generate_key()
        db.session.add(user)
        db.session.commit()
        return jsonify({"path": otpauth})
    else:
        return "where am I?"


def validate_user(user_json):
    #todo
    return True


if __name__ == "__main__":
    app.run()
