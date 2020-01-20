from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    github_id = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return '<User: {}>'.format(self.id)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(120))
    phone_number = db.Column(db.String(20))
    address_line_one = db.Column(db.String(60))
    address_line_two = db.Column(db.String(60))
    postcode = db.Column(db.String(10))

    def __repr__(self):
        return '<Profile: {}>'.format(self.id)
