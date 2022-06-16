from application import app, db
from flask import render_template, request, redirect, url_for
from application.forms import BasicForm, Register_1
from application.models import Genres, Songs, Users
import random
import pdb

@app.route ('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register_1():
     form = Register_1()
     
     if request.method == 'POST':
          first_name = Users(name=form.first_name.data)
     
          ##pdb.set_trace()
          if first_name == None:
               message = "Please supply your name!"
          else:
               db.session.add(first_name)
               db.session.commit()
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
          var1 = Genres.query.filter_by(name=form.favourite_1.data).first()
          var2 = Songs.query.filter_by(genre_id=var1.id).all()
          print(var1.id)
          for i in var2:
               print(i)
          return render_template('result.html', form=form, var2=var2)  
    
     else: 
               
          return render_template('result.html') 

@app.route('/input', methods=['GET', 'POST'])
def register():
    form = BasicForm()

    return render_template('input.html', form=form, message= "Riffbox")


