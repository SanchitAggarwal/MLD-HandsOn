#!/usr/bin/env python

""" A Simple Flask Server with a route to Recognise Faces
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

from flask import Flask, render_template, request, jsonify
from model import model_detect_face
import sys
import time
import os


def get_timpestamped_input_path():
    timestamp_string = time.strftime("%Y%m%d-%H%M%S")
    filename = timestamp_string + '_input.png'
    # input_image_path = os.path.join(os.getcwd(), input_data_directory, filename)
    print(filename)
    return filename


app = Flask(__name__)
@app.route('/')
def index(name=None):
    return render_template('index.html')

@app.route('/mode_face_recognition', methods=['GET', 'POST'])
def mode_face_recognition():
    if request.method == 'POST':
        try:
            f = request.files['file']
            input_image_path = get_timpestamped_input_path()
            f.save(input_image_path)
            results =  model_detect_face(input_image_path)
        except Exception as e:
            print(e)
            results = str(sys.exc_info()[0])
        return jsonify(results)

    elif request.method == 'GET':
        results = "Face Recognition End Point Hit Successfully"
        return jsonify(results)

if __name__ == '__main__':
	app.run(debug=True)
	