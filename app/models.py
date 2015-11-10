from app import db

class Player(db.Model):

    __tablename__ = 'mc_user'

    name        = db.Column(db.String(128), nullable=False)
    uuid        = db.Column(db.String(128), nullable=False, unique=True, primary_key=True)
    description = db.Column(db.Text(), nullable=True)
    role        = db.Column(db.String(128), nullable=False)
    last_login  = db.Column(db.DateTime, default=db.func.current_timestamp())

    # New instance instantiation procedure
    def __init__(self, name, uuid, description=None, role="player"):

        self.name        = name
        self.uuid        = uuid
        self.description = description
        self.role        = role

    def __repr__(self):
        return '<Player %r (%r | %r)>' % (self.name, self.role, self.uuid)  