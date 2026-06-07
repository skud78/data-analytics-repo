import pandas as pd

from analytics.timeseries.time_series_loader import load_timeseries
from analytics.timeseries.time_series_eda import ts_eda
from analytics.forecasting.forecasting_arima import train_arima, forecast_arima
from analytics.timeseries.evaluation_timeseries import evaluate_forecast

# 1. Load raw UCL data (not yet a time-series)
df = pd.read_csv("/home/sudhir/OneDrive/prof/comsci/ArtificialIntelligence/Machine Learning/sample-data/ucl_2025_26_clean.csv")

# 2. Feature engineering: create numeric target
df["total_goals"] = df["home_goals"] + df["away_goals"]

# 3. Convert to proper time-series using your loader
df_ts = load_timeseries(
    "/home/sudhir/OneDrive/prof/comsci/ArtificialIntelligence/Machine Learning/sample-data/ucl_2025_26_clean.csv",
    date_col="date"
)

# Replace the loaded numeric column with total_goals
df_ts["total_goals"] = df["total_goals"].values

# 4. EDA
ts_eda(df_ts)

# 5. Train ARIMA
model = train_arima(df_ts, target="total_goals", order=(1,1,1))

# 6. Forecast next 10 matchdays
pred = forecast_arima(model, steps=10)
print("\n=== FORECAST ===")
print(pred)

# 7. Optional evaluation (if you split actuals)
# metrics = evaluate_forecast(actual_series, pred)
# print(metrics)
