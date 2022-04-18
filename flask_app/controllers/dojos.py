from dataclasses import dataclass
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route('/')
def send_to_index():
    return redirect('/dojos')

@app.route('/dojos')
def index():
    dojos = Dojo.get_all()
    return render_template('index.html', all_dojos = dojos, session = session)

@app.route('/adding_dojo', methods = ['POST'])
def adding_dojo():
    data = {
        'name' : request.form['name']
    }
    
    Dojo.add_dojo(data)
    return redirect('/dojos')