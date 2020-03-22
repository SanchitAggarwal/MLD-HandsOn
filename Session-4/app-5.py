#!/usr/bin/env python

from flask import Flask, render_template
# create a Flask app variable
app = Flask(__name__)

#define a route
@app.route('/')
@app.route('/<modelname>')
def index(modelname="Default"):
	# rendering our simple html template with modelname
	return render_template('index.html', modelname=modelname)

if __name__ == '__main__':
	# running app in debug mode
	app.run(debug=True)