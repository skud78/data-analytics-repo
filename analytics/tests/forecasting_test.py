import pandas as pd
from analytics.evaluation import evaluate_forecast
from analytics.forecasting.forecasting_arima import train_arima, forecast_arima

# Fake time-series
df = pd.DataFrame({
    "date": pd.date_range(start="2024-01-01", periods=10, freq="D"),
    "value": [10, 12, 11, 13, 15, 14, 16, 18, 17, 19]
}).set_index("date")

model = train_arima(df, target="value", order=(1,1,1))
pred = forecast_arima(model, steps=3)

# Fake actuals for evaluation
actual = pd.Series([20, 21, 22])

metrics = evaluate_forecast(actual, pred)
print("Time-Series Test:", metrics)
