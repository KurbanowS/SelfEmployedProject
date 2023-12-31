from main import db
    

class Developers(db.Model):
    __searchable__ = ['name', 'email']
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    desc = db.Column(db.Text, nullable = False)

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


class Banners(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    def __repr__(self):
        return '<Banners {}>'.format(self.name)
    

