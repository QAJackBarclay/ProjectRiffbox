from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Genres, Songs

class TestBase(TestCase):
    def create_app(self):
                app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        #Adding Genres to db
        Genres = Genre(name="Techno")
        db.session.add(Genre)
        db.session.commit()
        
        #Adding Songs to db
        Skints2 = Songs(name="The Skints 2", playlist = reggae, link="https://youtu.be/DWWkzWisRTQ")
        db.session.add(Songs)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

