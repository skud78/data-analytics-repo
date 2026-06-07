import torch
from sklearn.metrics import accuracy_score

def evaluate_transformer(model, X_test, y_test):
    X_test = torch.tensor(X_test, dtype=torch.long)
    preds = model(X_test).detach().numpy().argmax(axis=1)
    y_true = y_test

    return {
        "accuracy": accuracy_score(y_true, preds)
    }
