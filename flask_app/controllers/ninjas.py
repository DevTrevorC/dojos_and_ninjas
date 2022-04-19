from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def	add_ninja():
	dojos = Dojo.get_all()
	return render_template('add_ninja.html', dojos = dojos)

@app.route('/ninjas/create', methods= ['POST'])
def	create_ninja():
	data = {
		"dojo_id" : request.form["dojo_id"],
		"first_name" : request.form["first_name"],
		"last_name" : request.form["last_name"],
		"age" : request.form["age"]
	}
	Ninja.new_ninja(data)
	return redirect('/dojos')