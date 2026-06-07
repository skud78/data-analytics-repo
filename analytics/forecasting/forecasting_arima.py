from statsmodels.tsa.arima.model import ARIMA

def train_arima(df, target: str, order=(1,1,1)):
    model = ARIMA(df[target], order=order)
    model_fit = model.fit()
    return model_fit

def forecast_arima(model_fit, steps=12):
    return model_fit.forecast(steps=steps)
