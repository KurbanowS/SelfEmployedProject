from main import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Me(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True )
    name = db.Column(db.String(6), nullable=False)
    email = db.Column(db.String(20), unique=True)
    password_hash = db.Column(db.String(40))

    def __repr__(self):
        return '<Me {}>'.format(self.name)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return Me.query.get(int(id))