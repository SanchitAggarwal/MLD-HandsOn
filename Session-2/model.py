#!/usr/bin/env python

""" A Face Recognition Model
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

import cv2
import sys
import argparse

def model_detect_face(input_image_path):
	feature_file_path = "haarcascade_frontalface_default.xml"
	feature_extractor = cv2.CascadeClassifier(feature_file_path)

	input_image = cv2.imread(input_image_path)
	gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)


	detected_faces = feature_extractor.detectMultiScale(
		gray_image,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(1,1),
		flags = cv2.CASCADE_SCALE_IMAGE
		)

	message = "Detected {0} faces!".format(len(detected_faces))
	print(message)

	# Draw green rectangles around the detected faces
	for (x, y, w, h) in detected_faces:
		cv2.rectangle(input_image, (x, y), (x+w, y+h), (0, 255, 0), 2)

	filename = 'output_' + input_image_path
	cv2.imwrite(filename, input_image)
	return message

if __name__ == '__main__':
	""" define cli arguments here"""
	parser = argparse.ArgumentParser()
	parser.add_argument('--inputimage_path', '-i', type=str, required=True)
	args = parser.parse_args()
	inputimage_path = args.inputimage_path
	model_detect_face(inputimage_path)