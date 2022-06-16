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

class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app


def tearDown(self):
    db.session.remove()
    db.drop_all()

class TestViewHome(TestBase):
    def test_get_home(self):
        response = self.client.get(url_for("index"))self.assert200(response)
   
    def setUp(self):
        # Create table
        db.create_all()
        # Create test registree
        first_name = Register(name="jack")
        # save users to database
        db.session.add(first_name)
        db.session.commit()

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

def test_basic_form(self):
    url_for('')
