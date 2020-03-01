#!/usr/bin/env python

""" A Simple Flask Server
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

from flask import Flask
app = Flask(__name__)


if __name__ == '__main__':
	app.run(debug=True)