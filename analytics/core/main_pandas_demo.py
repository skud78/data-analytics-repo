from analytics.core.pandas_utils import (
    load_csv, clean_missing, select_columns,
    group_and_aggregate, summary_stats
)

# Load dataset
df = load_csv("/home/sudhir/OneDrive/prof/comsci/ArtificialIntelligence/Machine Learning/sample-data/sales.csv")

# Clean missing values
df = clean_missing(df, strategy="fill", fill_value=0)

# Select columns
df_small = select_columns(df, ["region", "sales", "profit"])

# Group and aggregate
summary = group_and_aggregate(
    df_small,
    group_cols=["region"],
    agg_map={"sales": "sum", "profit": "mean"}
)

print("Summary:")
print(summary)

# Summary statistics
print("Stats:")
print(summary_stats(df_small))
