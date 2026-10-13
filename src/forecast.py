import numpy as np
from sklearn.linear_model import LinearRegression

def forecast_headcount(df, months_ahead=12):
    X = np.arange(len(df)).reshape(-1, 1)
    y = df["headcount"].values
    model = LinearRegression().fit(X, y)
    future_X = np.arange(len(df), len(df) + months_ahead).reshape(-1, 1)
    preds = model.predict(future_X)
    return preds.round(0).astype(int).tolist()
