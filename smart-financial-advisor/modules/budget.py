from sklearn.linear_model import LinearRegression
import numpy as np

def train_model(df):
    df = df.copy()
    df['month_index'] = range(len(df))

    X = df[['month_index']]
    y = df['amount']

    model = LinearRegression()
    model.fit(X, y)

    return model

def predict_next(model, next_index):
    pred = model.predict([[next_index]])
    return round(pred[0], 2)