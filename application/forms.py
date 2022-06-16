from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class Register_1(FlaskForm):
    first_name = StringField('What is your name?', validators=[Length(min=1, max=30),DataRequired()])
    submit = SubmitField('Enter site')

class BasicForm(FlaskForm):
    name = StringField("Your Name: ", validators=[DataRequired()])
    favourite_1 = SelectField("Pick a genre: ", choices = ['Rock', 'Metal', 'Reggae', 'Disco', 'Hardstyle', 'Rap'])
    submit = SubmitField ('Consult the Riffbox')