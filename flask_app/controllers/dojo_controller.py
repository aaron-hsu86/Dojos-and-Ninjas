from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo_model, ninja_model

@app.route('/dojos')
def main_page():
    dojos = dojo_model.Dojo.get_all()
    return render_template('dojos.html', dojos = dojos)

@app.route('/new_dojo', methods=['post'])
def new_dojo():
    dojo_model.Dojo.save(request.form)
    return redirect('/dojos')



@app.route('/show/<int:dojo_id>')
def show_dojo(dojo_id):
    dojo = dojo_model.Dojo.get_one(dojo_id)
    ninjas = ninja_model.Ninja.get_dojo_class(dojo_id)
    print(ninjas)
    return render_template('show_dojo.html', dojo=dojo, ninjas=ninjas)