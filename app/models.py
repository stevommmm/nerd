from app import db

class User(db.Model):

    __tablename__ = 'mc_user'

    name       = db.Column(db.String(128), nullable=False)
    uuid       = db.Column(db.String(128), nullable=False, unique=True)
    last_login = db.Column(db.DateTime, default=db.func.current_timestamp())

    # New instance instantiation procedure
    def __init__(self, name, email, password):

        self.name     = name
        self.uuid     = uuid

    def __repr__(self):
        return '<User %r (%r)>' % (self.name, self.uuid)  