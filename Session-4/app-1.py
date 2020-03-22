#!/usr/bin/env python

from flask import Flask
# create a Flask app variable
app = Flask(__name__)

@app.route('/')
def index():
	return "Our First <b>  Web APP </b> <br> First Tutorial on building a small App"

if __name__ == '__main__':
	# running app in debug mode
	app.run(debug=True)