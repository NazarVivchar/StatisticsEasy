import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def func(file, degree):
    df = pd.read_csv(file)
    X = df.iloc[:, 0].values
    y = df.iloc[:, 1].values
    X = np.array(X)
    X = X.reshape(-1, 1)
    y = np.array(y)
    y = y.reshape(-1, 1)
    train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=2)
    poly = PolynomialFeatures(degree=degree)
    lin_regressor = LinearRegression()
    X_poly = poly.fit_transform(train_X)
    lin_regressor.fit(X_poly, train_y)
    poly.fit(X_poly, train_y)

    predict_Y = lin_regressor.predict(poly.fit_transform(X))

    return predict_Y