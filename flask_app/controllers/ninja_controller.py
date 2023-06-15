from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import ninja_model, dojo_model

@app.route('/ninjas')
def new_ninja():
    dojos = dojo_model.Dojo.get_all()
    return render_template('ninjas.html', dojos = dojos)

@app.route('/add_ninja', methods=['post'])
def add_ninja():
    print(request.form)
    ninja_model.Ninja.save(request.form)
    return redirect('/dojos')