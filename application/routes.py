from application import app
from flask import render_template

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
    message = ""
    form = BasicForm()
    
    return render_template('home.html', form=form, message=message)