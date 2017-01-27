from flask import Flask, render_template

app = Flask(__name__)
from app import views

@app.errorhandler(404)
def not_found_error(error):
	return render_template('404.html',title='404')
