from demo import db
from demo import app
import hashlib, hmac     # for password hash
import pyotp


class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    nation = db.Column(db.String(10))
    club = db.Column(db.String(10))


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    password = db.Column(db.String(128))    # hashed
    department = db.Column(db.String(20))
    key = db.Column(db.String(16))      # key for token
    otpauth = db.Column(db.String(50))  # string to generate token

    def generate_key(self):
        self.key = pyotp.random_base32()
        t = pyotp.TOTP(self.key)
        self.otpauth = t.provisioning_uri(self.name)
        return self.otpauth

    def authenticate(self, otp):
        t = pyotp.TOTP(self.key)
        return t.verify(otp)

    def hash_password(self, password):
        h = hmac.new(app.secret_key, password, hashlib.sha256)
        self.password = h.hexdigest()

    def verify_password(self, password):
        h = hmac.new(app.secret_key, password, hashlib.sha256)
        hash_password = h.hexdigest()
        if(self.password == hash_password):
            return True
        else:
            return False
