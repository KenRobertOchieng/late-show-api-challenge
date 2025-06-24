from server.app import db

class Episode(db.Model):
    __tablename__ = 'episode'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete-orphan')  # ✅ This must match Appearance
