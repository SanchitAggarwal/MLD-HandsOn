#!/usr/bin/env python

from flask import Flask, render_template, request

# create a Flask app variable
app = Flask(__name__)

#define a route

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
	if request.method == 'POST':
		return "POST REQUEST"
	else:
		return "GET REQUEST"

if __name__ == '__main__':
	# running app in debug mode
	app.run(debug=True)
