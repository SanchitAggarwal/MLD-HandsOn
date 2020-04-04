#!/usr/bin/env python

from flask import Flask, render_template
# create a Flask app variable
app = Flask(__name__)

#define a route
@app.route('/')
def index():
	# rendering our simple html template
	return render_template('index.html')

if __name__ == '__main__':
	# running app in debug mode
	app.run(debug=True)