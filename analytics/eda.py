import pandas as pd

def quick_eda(df: pd.DataFrame):
    print("\n=== SHAPE ===")
    print(df.shape)

    print("\n=== DATA TYPES ===")
    print(df.dtypes)

    print("\n=== MISSING VALUES ===")
    print(df.isna().sum())

    print("\n=== SUMMARY STATS ===")
    print(df.describe(include="all"))
