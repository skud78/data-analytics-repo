import pandas as pd
from sklearn.linear_model import LinearRegression

from analytics.evaluation import evaluate_regression

# Fake regression dataset
df = pd.DataFrame({
    "x1": [1, 2, 3, 4, 5],
    "x2": [2, 1, 3, 5, 4],
    "y":  [3, 4, 6, 8, 9]
})

X = df[["x1", "x2"]]
y = df["y"]

model = LinearRegression().fit(X, y)

metrics = evaluate_regression(model, X, y)
print("Regression Test:", metrics)
