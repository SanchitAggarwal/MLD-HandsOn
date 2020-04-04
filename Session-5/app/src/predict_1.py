#!/usr/bin/env python

import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from src.feature import data_selection, data_preprocessing, feature_extractor


selected_variables = ["YearBuilt", "BedroomAbvGr", "KitchenAbvGr"]
target_varibale = ["SalePrice"]
model_path = "../output/model_1.pkl"
dataset_path = "../dataset/test.csv"

def read_model(model_path="../output/model.pkl"):
	 # function to read model
	 message = "function to read model"
	 model = joblib.load(model_path)
	 return model

def predict_price(features, model):
	# function to predict for give feature/features
	message = "function to predict for give feature/features"
	predicted_labels = model.predict(features)
	return predicted_labels

if __name__ == '__main__':
    message = "defining stubs"
    print (message)
     # read data
    data = pd.read_csv(dataset_path)
    print(data.shape)
    print(data.head(5))
    
    # data selection
    data = data_selection(data, selected_variables)
    print(data.shape)
    print(data.head(5))

    # data preprocessing
    data = data_preprocessing(data)
    print(data.shape)
    print(data.head(5))

    data[target_varibale[0]] = 0
    print(data.shape)
    print(data.head(5))

    # feature extractor
    featueres, label = feature_extractor(data)
    print(featueres.shape)
    print(featueres.head(5))
    print(label.shape)
    print(label.head(5))

    model = read_model(model_path)
    predicted_labels = predict_price(featueres, model)
    print(predicted_labels)