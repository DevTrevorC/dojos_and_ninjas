from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def	add_ninja():
	return render_template('add_ninja.html')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    return render_template('show_dojo.html')