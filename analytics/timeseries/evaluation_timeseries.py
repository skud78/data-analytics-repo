from sklearn.metrics import mean_squared_error, mean_absolute_error

def evaluate_forecast(actual, predicted):
    return {
        "mae": mean_absolute_error(actual, predicted),
        "rmse": mean_squared_error(actual, predicted, squared=False)
    }
