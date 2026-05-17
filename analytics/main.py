from sklearn.metrics import (
    mean_squared_error,
    r2_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

def evaluate_regression(model, X_test, y_test):
    preds = model.predict(X_test)
    return {
        "rmse": mean_squared_error(y_test, preds, squared=False),
        "r2": r2_score(y_test, preds)
    }

def evaluate_classification(model, X_test, y_test):
    preds = model.predict(X_test)
    return {
        "accuracy": accuracy_score(y_test, preds),
        "precision": precision_score(y_test, preds, average="weighted"),
        "recall": recall_score(y_test, preds, average="weighted"),
        "f1": f1_score(y_test, preds, average="weighted")
    }
