from main import db

class Me(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(6))
    email = db.Column(db.String(20))
    desc = db.Column(db.Text)
    links = db.Column(db.String(120))

    def __repr__(self):
        return '<Me {}>'.format(self.name)
    