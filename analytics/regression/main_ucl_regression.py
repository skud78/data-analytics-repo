from analytics.dataprep.data_loader import load_data
from analytics.dataprep.data_cleaning import clean_dataframe
from analytics.eda import quick_eda
from analytics.regression.linear_regression import train_linear_regression
from analytics.evaluation import evaluate_regression

df = load_data ("/home/sudhir/OneDrive/prof/comsci/ArtificialIntelligence/Machine Learning/sample-data/ucl_2025_26_clean.csv")
df = clean_dataframe(df)

quick_eda(df)
# Optional: add engineered features
df["total_goals"] = df["home_goals"] + df["away_goals"]


import pandas as pd

# 1. Convert date column safely
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

# 2. Drop time column (not useful for regression)
if "time" in df.columns:
    df.drop(columns=["time"], inplace=True)

# 3. Convert numeric-looking columns only
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="ignore")

# 4. Select numeric columns for regression
numeric_df = df.select_dtypes(include=["number"]).copy()

# 5. Ensure target exists
if "total_goals" not in numeric_df.columns:
    raise ValueError("target 'total_goals' must be numeric after cleaning")

# Keep only numeric columns
df_numeric = df.select_dtypes(include=["number"]).copy()
model, splits = train_linear_regression(df_numeric, target="total_goals")


metrics = evaluate_regression(model, splits["X_test"], splits["y_test"])
print(metrics)
