# This is a linier regression python practice with stock price as dataset
import numpy as np
import pandas as pd
import quandl
import math
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = quandl.get("WIKI/GOOGL")
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
print(df.head())

# Speread based on the closing price
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0

# Daily percent change
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / \
    df['Adj. Open'] * 100.0

df1 = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
print(df1.head)

forecast_col = 'Adj. Close'
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
