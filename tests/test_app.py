from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Genres, Songs

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
    
    def setUp(self):
        db.create_all()
        #Adding Genres to db
        test_genres = Genres(name="Reggae")
        db.session.add(test_genres)
        db.session.commit()
        
        #Adding Songs to db
        Skints2 = Songs(name="The Skints 2",genre_id = 1, link="https://youtu.be/DWWkzWisRTQ")
        db.session.add(Skints2)
        db.session.commit()

class TestViewHome(TestBase):
    def test_get_home(self):
        response = self.client.get(url_for("index"))
        self.assert200(response)

class TestViewResults(TestBase):
    def test_get_results(self):
        response = self.client.get(url_for("result"))
        self.assert200(response)

    #def test_basic_form(self):
       # url_for('')
