import numpy as np
import os
import sys
def clean_data(data, column_of_interest, default_column):
    print("Cleaning Data ...")
    data = data.drop_duplicates()
    data = data.dropna(subset=[column_of_interest], how="any")
    data[default_column].fillna(0, inplace=True)
    print("Data Cleaning Task is Completed")
    return data
def clean_data2(data):
    data.fillna(data.mean(numeric_only=True), inplace=True)
    return data
def treat_outlier_with_mean(column):
    Q1=column.quantile(0.25)
    Q3=column.quantile(0.75)
    IQR=Q3-Q1
    lower_bound=Q1-1.5*IQR
    upper_bound=Q3+1.5*IQR

    column_mean=column.mean()
    column=np.where((column<lower_bound) | (column>upper_bound), column_mean, column)

    return column


