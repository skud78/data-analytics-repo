import pandas as pd

def moving_average_forecast(df, target: str, window=3, steps=12):
    last_values = df[target].tail(window)
    avg = last_values.mean()
    future = [avg] * steps
    return pd.Series(future)
