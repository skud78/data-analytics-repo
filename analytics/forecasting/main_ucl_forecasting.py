import pandas as pd

from analytics.dataprep.data_loader import load_data
from analytics.dataprep.data_cleaning import clean_dataframe
from analytics.forecasting.forecasting_arima import train_arima, forecast_arima

# 1. Load + clean
df = load_data("/home/sudhir/OneDrive/prof/comsci/ArtificialIntelligence/Machine Learning/sample-data/ucl_2025_26_clean.csv")
df = clean_dataframe(df)

# 2. Convert date
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.sort_values("date")

# 3. Feature engineering
df["total_goals"] = df["home_goals"] + df["away_goals"]

# 4. Build time-series
ts = df[["date", "total_goals"]].set_index("date")

# 5. Train ARIMA model
model = train_arima(ts, target="total_goals", order=(1,1,1))

# 6. Forecast next 10 matchdays
forecast = forecast_arima(model, steps=10)

print("=== UCL Goal Forecast ===")
print(forecast)
