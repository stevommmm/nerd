from app import db

class Player(db.Model):

    __tablename__ = 'mc_user'

    name        = db.Column(db.String(128), nullable=False)
    uuid        = db.Column(db.String(128), nullable=False, unique=True, primary_key=True)
    description = db.Column(db.Text(), nullable=True)
    last_login  = db.Column(db.DateTime, default=db.func.current_timestamp())

    # New instance instantiation procedure
    def __init__(self, name, uuid, description=None):

        self.name        = name
        self.uuid        = uuid
        self.description = description

    def __repr__(self):
        return '<Player %r (%r)>' % (self.name, self.uuid)  