def clustering_eda(df):
    print("\n=== SHAPE ===")
    print(df.shape)

    print("\n=== SUMMARY ===")
    print(df.describe())

    print("\n=== CORRELATION MATRIX ===")
    print(df.corr())
