from main import db


class Me(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    name = db.Column(db.String(6))
    email = db.Column(db.String(20))
    desc = db.Column(db.Text)
    links = db.Column(db.String(120))

    def __repr__(self):
        return '<Me {}>'.format(self.name)
    

class Developers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    desc = db.Column(db.Text, nullable = False,)

    def __repr__(self):
        return '<Developers {}>'.format(self.name)
    

    def to_dict(self):
        data = {
            'id' : self.id,
            'name' : self.name,
            'email' : self.email,
            'desc' : self.desc
        }
        return data
    
    def from_dict(self, data):
        for field in ['name', 'email', 'desc']:
            if field in data:
                setattr(self, field, data[field])