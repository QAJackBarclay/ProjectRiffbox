from application import app
from flask import render_template
from application.forms import BasicForm


@app.route ('/')

@app.route('/home')
def home():
     return render_template('home.html')

@app.route('/index')
def index():
     return render_template('index.html')

@app.route('/instructions')
def instructions():
     return render_template('instructions.html')

@app.route('/result')
def result():
     return render_template('result.html')

@app.route('/input', methods=['GET', 'POST'])
def register():
    form = BasicForm()
    
    return render_template('input.html', form=form, message= "Riffbox")