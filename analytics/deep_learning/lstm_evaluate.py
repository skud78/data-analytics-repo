import torch
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_lstm(model, X_test, y_test):
    X_test = torch.tensor(X_test, dtype=torch.float32)
    preds = model(X_test).detach().numpy().flatten()
    y_true = y_test.flatten()

    return {
        "rmse": mean_squared_error(y_true, preds) ** 0.5,
        "r2": r2_score(y_true, preds)
    }
