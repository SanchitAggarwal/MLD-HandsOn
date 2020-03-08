#!/usr/bin/env python

from flask import Flask
# create a Flask app variable
app = Flask(__name__)

@app.route('/')
def index():
	return "<h1> Our First Web APP</h1>"

if __name__ == '__main__':
	# running app in debug mode
	app.run(debug=True)