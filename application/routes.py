from application import app
from flask import render_template, request, redirect, url_for
from application.forms import BasicForm, Register_1
from application.models import Genres, Songs
import random

@app.route ('/', methods=['GET', 'POST'])

#@app.route('/home')
#def home():
#return render_template('home.html', form=form, message=message)

@app.route('/home', methods=['GET', 'POST'])
def register_1():
     form = Register_1()
     
     if request.method == 'POST':
          first_name = form.first_name.data

          if len(first_name) == 0:
               message = "Please supply your name!"
          else:
               message = f'Thank you, {first_name}'
               return redirect(url_for("register"))

     return render_template('home.html', form=form)

@app.route('/index')
def index():
     return render_template('index.html')

@app.route('/instructions')
def instructions():
     return render_template('instructions.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
     form = BasicForm()
     if request.method == 'POST':
    #dark_souls = Games.query.filter_by(name="Dark Souls").all()
          var1 = Genres.query.filter_by(name=form.favourite_1.data).first()  #, playlist=form.favourite_1.data, link=form.favourite_1.data)
          var2 = Songs.query.filter_by(genre_id=var1.id).all()
          var2 = Songs.query.all()
          print(var1.id)
          for i in var2:
               print(i)

     return render_template('result.html', var1=var1, form=form, var2=var2)

@app.route('/input', methods=['GET', 'POST'])
def register():
    form = BasicForm()

    return render_template('input.html', form=form, message= "Riffbox")


