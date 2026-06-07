from data_loader import load_data
from data_cleaning import clean_dataframe
from eda import quick_eda
from analytics.regression.linear_regression import train_linear_regression
from evaluation import evaluate_regression

df = load_data("/home/sudhir/OneDrive/prof/sw/data-analytics/housing.csv")
df = clean_dataframe(df)
quick_eda(df)

model, splits = train_linear_regression(df, target="price")
metrics = evaluate_regression(model, splits["X_test"], splits["y_test"])
print(metrics)
