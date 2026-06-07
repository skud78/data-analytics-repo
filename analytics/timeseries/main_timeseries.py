from analytics.timeseries.time_series_loader import load_timeseries
from analytics.timeseries.time_series_eda import ts_eda
from analytics.forecasting.forecasting_arima import train_arima, forecast_arima
from analytics.timeseries.evaluation_timeseries import evaluate_forecast

# 1. Load
df = load_timeseries("/home/sudhir/OneDrive/prof/sw/data-analytics/sales_timeseries.csv")

# 2. EDA
ts_eda(df)

# 3. Train ARIMA
model = train_arima(df, target="sales", order=(1,1,1))

# 4. Forecast next 6 months
pred = forecast_arima(model, steps=6)
print(pred)

# 5. Evaluate (if you have actuals)
# metrics = evaluate_forecast(actual_series, pred)
# print(metrics)
