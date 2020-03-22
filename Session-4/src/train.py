#!/usr/bin/env python

import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold


# defining global variable
feature_path = "../output/feature.csv"
label_path = "../output/label.csv"


def read_data(filename):
    # function to read features or labels
    return pd.read_csv(filename)


def train_linear_model(features, labels):
    # function to select data
    message = "function to select data"
    print("learning model...")
    model = LinearRegression(fit_intercept=True, normalize=True)
    # fit a model
    return model.fit(features, labels)


def cross_validation(features, labels, folds=10, seed=1, shuffle=True):
    # function for data pre-processing
    message = "function for data pre-processing"
    kf = KFold(n_splits=folds, random_state=seed, shuffle=True)
    model = LinearRegression(fit_intercept=True, normalize=True)
    model_errors = []
    models = []
    for training_index, validation_index in kf.split(features):
    	train_x = features.iloc[training_index]
    	train_y_actual = labels.iloc[training_index]

    	val_x = features.iloc[validation_index]
    	val_y_actual = labels.iloc[validation_index]

    	# fit a model
    	model.fit(train_x, train_y_actual)
    	# test the model on validation set
    	val_y_predicted = model.predict(val_x)

    	model_error = evaluation(val_y_actual, val_y_predicted)
    	message = "model error for current run is: " + str(model_error) 
    	print(message)
    	model_errors.append(model_error)
    	models.append(model)
    	# visualise_model(val_x, val_y_actual, val_y_predicted, model_error)
    
    minimum_error = min(model_errors)
    minimum_error_index = model_errors.index(minimum_error)
    model_with_minimum_error = models[minimum_error_index]
    return model_with_minimum_error


def visualise_model(features, actual_labels, predicted_labels, model_error, destination_filepath="../output/graph.png"):
    plt.scatter(features, actual_labels, color='orange')
    plt.plot(features, predicted_labels, color='blue', linewidth=2)
    plt.legend(loc='lower right')
    plt.xlabel("Feature X")
    plt.ylabel("Sale Price")
    plt.title("Graph for prediction and actual data")
    plt.savefig(destination_filepath+model_error+".png")
    plt.close()
    message = "saved graph at... " + destination_filepath
    print(message)

def evaluation(actual, predicted):
    # function for feature_extractor
    message = "function for feature_extractor"
    model_error = mean_squared_error(actual, predicted)    
    return np.sqrt(model_error)

def save_model(model, modelpath = "../output/model.pkl"):
	# function for saving_model
	message  = "function for saving_model"
	joblib.dump(model, modelpath)
	message = "saved model at... " + modelpath
	print(message)


if __name__ == '__main__':
    message = "defining stubs"
    print (message)
    # read data
    features = read_data(feature_path)
    labels = read_data(label_path)
    print(features.shape)
    print(features.head(5))
    print(labels.shape)
    print(labels.head(5))

    model_with_minimum_error = cross_validation(features, labels)
    save_model(model_with_minimum_error)
