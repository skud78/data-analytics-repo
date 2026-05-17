import pandas as pd
import numpy as np

def clean_dataframe(df: pd.DataFrame):
    df = df.copy()

    # Strip whitespace from column names
    df.columns = df.columns.str.strip()

    # Drop duplicate rows
    df = df.drop_duplicates()

    # Replace blank strings with NaN
    df = df.replace(r'^\s*$', np.nan, regex=True)

    # Convert numeric-looking columns
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except Exception:
            pass
        
    return df
