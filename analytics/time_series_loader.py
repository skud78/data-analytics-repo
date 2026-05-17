import pandas as pd

def load_timeseries(path: str, date_col: str = "date"):
    df = pd.read_csv(path)
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.set_index(date_col).sort_index()
    return df
