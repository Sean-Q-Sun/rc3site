from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html', title='Home')

@app.route('/sponsors')
def sponsors():
	return render_template('sponsors.html', title='Sponsors')

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/this-week')
def tw():
	return render_template('this-week.html', title='This Week')

@app.route('/community')
def community():
	return render_template('community.html', title='Community')

@app.route('/competitions')
def competitions():
	return render_template('competitions.html', title='Competitions')

@app.route('/hall-of-fame')
def hallOfFame():
	return "Hall of Fame"

# mostly here for testing purposes
@app.route("/dashboard")
def userDashboard():
		return render_template("dashboard.html")
