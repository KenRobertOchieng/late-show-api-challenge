from server.app import app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

with app.app_context():
    # Re-create database schema
    db.drop_all()
    db.create_all()

    # New guests
    g1 = Guest(name="Scarlett Johansson", occupation="Actor")
    g2 = Guest(name="Neil deGrasse Tyson", occupation="Astrophysicist")
    g3 = Guest(name="Serena Williams", occupation="Athlete")

    # New episodes
    e1 = Episode(date="2025-07-01", number=101)
    e2 = Episode(date="2025-07-02", number=102)
    e3 = Episode(date="2025-07-03", number=103)

    # Appearances linking guests to episodes
    a1 = Appearance(rating=5, guest=g1, episode=e1)
    a2 = Appearance(rating=4, guest=g2, episode=e2)
    a3 = Appearance(rating=5, guest=g3, episode=e3)

    # Commit all
    db.session.add_all([g1, g2, g3, e1, e2, e3, a1, a2, a3])
    db.session.commit()
