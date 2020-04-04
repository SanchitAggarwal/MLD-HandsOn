#!/usr/bin/env python

from flask import Flask, render_template, request
from src.feature import data_preprocessing, feature_extractor
from src.predict import read_model, predict_price
import pandas as pd
import numpy as np

# create a Flask app variable
app = Flask(__name__)

#define a route

@app.route('/<modelname>')
def index(modelname="Default"):
	# rendering our simple html template with modelname
	return render_template('index.html', modelname=modelname)

@app.route('/')
@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
	if request.method == 'POST':
		data = [int(x) for x in request.form.values()]
		data = np.array([data])
		print(data)
		data_df = pd.DataFrame(data=data, columns=["YearBuilt", "BedroomAbvGr", "KitchenAbvGr"])
		# data_df = pd.DataFrame()
		# data_df["YearBuilt"] = data[0]
		# data_df["BedroomAbvGr"] = data[1]
		# data_df["KitchenAbvGr"] = data[2]
		print("data frame after assigning values", data_df.head())
		# data preprocessing
		data_df = data_preprocessing(data_df)
		data_df["SalePrice"] = 0

		# feature extractor
		features, label = feature_extractor(data_df)
		model = read_model("output/model_1.pkl")
		label = predict_price(features, model)
		print(label)
		return render_template('houseprice.html', predicted_house_price='House Price should be $ {}'.format(label[0][0]))
	else:
		return render_template('houseprice.html')

if __name__ == '__main__':
	# running app in debug mode
	app.run(debug=True)
