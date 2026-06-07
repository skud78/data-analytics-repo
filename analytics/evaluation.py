from sklearn.metrics import (
    mean_squared_error,
    r2_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    silhouette_score
)

# -----------------------------
# REGRESSION
# -----------------------------
def evaluate_regression(model, X_test, y_test):
    preds = model.predict(X_test)
    return {
        "rmse": mean_squared_error(y_test, preds) ** 0.5,
        "r2": r2_score(y_test, preds)
    }

# -----------------------------
# CLASSIFICATION
# -----------------------------
def evaluate_classification(model, X_test, y_test):
    preds = model.predict(X_test)
    return {
        "accuracy": accuracy_score(y_test, preds),
        "precision": precision_score(y_test, preds, average="weighted"),
        "recall": recall_score(y_test, preds, average="weighted"),
        "f1": f1_score(y_test, preds, average="weighted")
    }

# -----------------------------
# TIME-SERIES FORECASTING
# -----------------------------
def evaluate_forecast(actual, predicted):
    return {
        "mae": mean_squared_error(actual, predicted) ** 0.5,
        "rmse": mean_squared_error(actual, predicted) ** 0.5
    }

# -----------------------------
# CLUSTERING
# -----------------------------
def evaluate_clustering(data, labels):
    return {
        "silhouette": silhouette_score(data, labels)
    }
