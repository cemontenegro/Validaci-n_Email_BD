from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario_model import Usuario
from flask_app import app


@app.route('/')
def index():
	return render_template("index.html")


@app.route('/process',methods=['POST'])
def process():
	session['email'] = request.form['email']

	if not Usuario.is_valid(request.form):
		return redirect('/')
	Usuario.save(request.form)
	return redirect('/results')


@app.route('/results')
def results():
	return render_template("results.html",usuarios=Usuario.get_all())

@app.route('/destroy/<int:id>')
def destroy_email(id):
	data = {
		"id": id
	}
	Usuario.destroy(data)
	return redirect('/results')