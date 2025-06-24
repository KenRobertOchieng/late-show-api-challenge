from server.app import db

class Appearance(db.Model):
    __tablename__ = 'appearance'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), nullable=False)

    guest = db.relationship('Guest', back_populates='appearances')
    episode = db.relationship('Episode', back_populates='appearances')  # ✅ THIS IS REQUIRED

    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "guest_id": self.guest_id,
            "guest_name": self.guest.name if self.guest else None,
            "episode_id": self.episode_id,
            "episode_number": self.episode.number if self.episode else None
        }
