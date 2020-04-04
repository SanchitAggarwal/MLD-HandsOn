#!/usr/bin/env python

from flask import Flask, render_template, request, redirect
from src.feature import data_preprocessing, feature_extractor
import pandas as pd
import numpy as np

# create a Flask app variable
app = Flask(__name__)

#define a route

# @app.route('/<modelname>')
# def index(modelname="Default"):
# 	# rendering our simple html template with modelname
# 	return render_template('index.html', modelname=modelname)

@app.route('/')
@app.route('/select_model', methods=['GET', 'POST'])
def select_model():
	# rendering our select model html template
	if request.method == 'POST':
		option = request.form['options']
		print(option)
		if option == "Model_1":
			return redirect('/prediction')
		else:
			return redirect('/prediction_2')
		print("select a model")
		# 
	else:
		return render_template('select_model.html')
	

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
	from src.predict_1 import read_model, predict_price
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

@app.route('/prediction_2', methods=['GET', 'POST'])
def prediction_2():
	from src.predict_2 import read_model, predict_price
	if request.method == 'POST':
		data = [int(x) for x in request.form.values()]
		data = np.array([data])
		print(data)
		data_df = pd.DataFrame(data=data, columns=["YearBuilt", "BedroomAbvGr", "KitchenAbvGr", "GarageYrBlt", "GarageCars", "GarageArea", "PoolArea"])
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
		model = read_model("output/model_2.pkl")
		label = predict_price(features, model)
		print(label)
		return render_template('houseprice_with_garage.html', predicted_house_price='House Price should be $ {}'.format(label[0][0]))
	else:
		return render_template('houseprice_with_garage.html')


@app.route('/training', methods=['GET', 'POST'])
def Training():
	"stubs for taining"

if __name__ == '__main__':
	# running app in debug mode
	app.run(debug=True)
