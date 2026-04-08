import pandas as pd

def load_data(file):
    df = pd.read_csv(file)
    return df

def category_summary(df):
    return df.groupby("category")["amount"].sum()

def monthly_summary(df):
    df['date'] = pd.to_datetime(df['date'])
    return df.groupby(df['date'].dt.month)['amount'].sum() 