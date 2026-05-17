import pandas as pd
from pathlib import Path

def load_data(path: str):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix == ".csv":
        df = pd.read_csv(path)
    elif path.suffix == ".parquet":
        df = pd.read_parquet(path)
    else:
        raise ValueError("Unsupported file type")

    print(f"Loaded {df.shape[0]} rows × {df.shape[1]} columns")
    return df
