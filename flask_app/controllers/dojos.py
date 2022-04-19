from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route('/')
def send_to_index():
    return redirect('/dojos')

@app.route('/dojos')
def index():
    dojos = Dojo.get_all()
    return render_template('index.html', all_dojos = dojos)

@app.route('/adding_dojo', methods = ['POST'])
def adding_dojo():
    data = {
        'name' : request.form['name']
    }
    Dojo.add_dojo(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    print('show dojo')
    data = {
        'id' : id
    }
    dojo = Dojo.get_one(data)
    print(dojo)
    print('tooooooooooooooooooooooooooooooooooooooodddddddddddddddddddddddddddddddddddd')
    return render_template('show_dojo.html', dojo = dojo)