#!/usr/bin/env python

""" A Simple Flask Server with a route
This program is developed by Ayata Intelligence Private Limited.
This program is proprietary software: you cannot redistribute it and/or modify it.
"""

__author__ = "Ayata Intelligence Private Limited"
__copyright__ = "Copyright 2020, Ayata Intelligence Private Limited"
__credits__ = ["Sanchit"]
__date__ = "2020/03/01"
__license__ = "proprietary"
__maintainer__ = "Ayata Intelligence Private Limited"
__status__ = "Development"
__version__ = "1.0.0"

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def first_route():
	return 'Created First Route!'

@app.route('/get_route', methods=['GET'])
def get_route():
    if request.method == 'GET':
        return 'Created First GET Route!'

@app.route('/post_my_message', methods=['POST'])
def post_my_message():
    if request.method == 'POST':
        return 'Created First POST Route!'


if __name__ == '__main__':
	app.run(debug=True)