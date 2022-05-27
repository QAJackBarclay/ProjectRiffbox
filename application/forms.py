from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class BasicForm(FlaskForm):
    name = StringField("Your Name: ", validators=[DataRequired()])
    favourite_1 = SelectField("Pick a genre: ", choices = ['Rock', 'Metal', 'Reggae', 'Disco', 'Hardstyle' ])
    favourite_2 = SelectField("Pick a genre: ", choices = ['Rock', 'Metal', 'Reggae', 'Disco', 'Hardstyle'])
    favourite_3 = SelectField("Pick a genre: ", choices = ['Rock', 'Metal', 'Reggae', 'Disco', 'Hardstyle'])
    submit = SubmitField ('Consult the Riffbox')