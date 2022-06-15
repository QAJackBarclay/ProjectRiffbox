from application import db

class Genres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    playlists = db.relationship('Songs', backref='playlist')

class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    link = db.Column(db.String(50))
    genre_id=db.Column(db.Integer, db.ForeignKey("genres.id"))
#    playlists = db.relationship('Playlists', backref='genres')

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))