import matplotlib
matplotlib.use("Agg")   # correct backend setting

import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# BASIC LINE PLOT
# -----------------------------
def plot_line(x, y, title="", xlabel="", ylabel="", grid=True, filename="plot_line.png"):
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker="o")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if grid:
        plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# -----------------------------
# SCATTER PLOT
# -----------------------------
def plot_scatter(x, y, title="", xlabel="", ylabel="", grid=True, filename="plot_scatter.png"):
    plt.figure(figsize=(10, 5))
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if grid:
        plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# -----------------------------
# HISTOGRAM
# -----------------------------
def plot_histogram(data, bins=20, title="", xlabel="", ylabel="Frequency", filename="plot_histogram.png"):
    plt.figure(figsize=(10, 5))
    plt.hist(data, bins=bins, edgecolor="black")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# -----------------------------
# BOXPLOT
# -----------------------------
def plot_boxplot(data, labels=None, title="", filename="plot_boxplot.png"):
    plt.figure(figsize=(8, 5))
    plt.boxplot(data, labels=labels)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# -----------------------------
# BAR CHART
# -----------------------------
def plot_bar(categories, values, title="", xlabel="", ylabel="", filename="plot_bar.png"):
    plt.figure(figsize=(10, 5))
    plt.bar(categories, values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# -----------------------------
# TIME SERIES PLOT
# -----------------------------
def plot_timeseries(dates, values, title="", xlabel="Date", ylabel="Value", filename="plot_timeseries.png"):
    plt.figure(figsize=(12, 5))
    plt.plot(dates, values, marker="o")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# -----------------------------
# CORRELATION HEATMAP
# -----------------------------
def plot_correlation_heatmap(df, title="Correlation Heatmap", filename="plot_corr_heatmap.png"):
    numeric_df = df.select_dtypes(include=["number"])  # FIX: only numeric columns
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
