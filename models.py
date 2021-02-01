from main import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), unique=False, nullable=False)
    lastname = db.Column(db.String(50), unique=False, nullable=False)
    dob = db.Column(db.String(50), unique=False, nullable=False)
    Residential = db.Column(db.String(50), unique=False, nullable=False)
    Nationality = db.Column(db.String(50), unique=False, nullable=False)
    nin = db.Column(db.String(50), unique=False, nullable=False)


    def __repr__(self):
        return "<Register {}>".format(self.id)