from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html', title='Home')

@app.route('/sponsors')
def sponsors():
	return "Sponsors!"

@app.route('/about')
def about():
	return "About Page"

@app.route('/this-week')
def tw():
	return "This Week"

@app.route('/community')
def community():
	return "Community"

@app.route('/competitions')
def competitions():
	return "Competitions page"

@app.route('/hall-of-fame')
def hallOfFame():
	return "Hall of Fame"
