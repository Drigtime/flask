from flask import Flask, render_template
from http import HTTPStatus

app = Flask(__name__)

from utils.bundle import assets

@app.route('/')
def index():
	return render_template('index.jinja')

@app.route('/tutu')
def tutu():
	return render_template('tutu.jinja')

@app.route('/matiere')
def matiere():
	return render_template('matiere.jinja')

@app.route('/hello')
def hello():
        return 'Hello'

@app.route('/hello/<name>')
def helloUser(name):
	return 'Hello {} !'.format(name), HTTPStatus.CREATED

@app.route('/add/<int:left>/<int:right>')
def add(left, right):
	return str(left + right)

@app.errorhandler(404)
def error404(e):
	return '404 not found'
