#!/usr/bin/env python

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# defining global variable
dataset_path = "../dataset/train.csv"
selected_variables = ["YearBuilt", "BedroomAbvGr", "KitchenAbvGr", "SalePrice"]
target_varibale = ["SalePrice"]

def data_selection(data, selected_variables):
    # function to select data
    data = data[selected_variables]
    return data

def data_validation():
    # function to select data
    message = "function for data validation"

def data_preprocessing():
    # function for data pre-processing
    message = "function for data preprocessing"

def feature_extractor():
    # function for feature_extractor
    message = "function for feature extractor"

def data_split():
    # function for splitting data into training and testing
    message = "function for data split"

if __name__ == '__main__':
    # read data
    data = pd.read_csv(dataset_path)
    print(data.shape)
    print(data.head(5))
    
    # data selection
    data = data_selection(data, selected_variables)
    print(data.shape)
    print(data.head(5))