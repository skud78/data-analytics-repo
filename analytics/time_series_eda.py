def ts_eda(df):
    print("\n=== SHAPE ===")
    print(df.shape)

    print("\n=== DATE RANGE ===")
    print(df.index.min(), "→", df.index.max())

    print("\n=== SUMMARY ===")
    print(df.describe())

    print("\n=== MISSING VALUES ===")
    print(df.isna().sum())
