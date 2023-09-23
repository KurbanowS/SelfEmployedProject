from main import db

class Designers(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), nullable=False, primary_key=True)
    email = db.Column(db.String(40), nullable=False, primary_key=True)
    desc = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Designers> {}'.format(self.name)
    

    def to_dictt(self):
        data = {
            'id' : self.id,
            'name' : self.name,
            'email' : self.email,
            'desc' : self.desc
        }
        return data
    
    def from_dictt(self, data):
        for field in ['name', 'email', 'desc']:
            if field in data:
                setattr(self, field, data[field])