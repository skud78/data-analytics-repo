
import pandas as pd
from analytics.core.viz_matplotlib import (
    plot_line, plot_scatter, plot_histogram,
    plot_boxplot, plot_bar, plot_timeseries,
    plot_correlation_heatmap
)

# Example dataset
df = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "sales": [120, 150, 170, 160, 200],
    "profit": [30, 40, 45, 38, 55]
})

# Line plot
plot_line(df["month"], df["sales"], title="Monthly Sales", xlabel="Month", ylabel="Sales")

# Scatter plot
plot_scatter(df["sales"], df["profit"], title="Sales vs Profit", xlabel="Sales", ylabel="Profit")

# Histogram
plot_histogram(df["sales"], bins=5, title="Sales Distribution", xlabel="Sales")

# Boxplot
plot_boxplot([df["sales"], df["profit"]], labels=["Sales", "Profit"], title="Sales & Profit Spread")

# Bar chart
plot_bar(df["month"], df["sales"], title="Sales by Month", xlabel="Month", ylabel="Sales")

# Time series
plot_timeseries(df["month"], df["sales"], title="Sales Trend")

# Correlation heatmap
plot_correlation_heatmap(df)
