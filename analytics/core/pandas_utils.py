import pandas as pd

# -----------------------------
# LOADING
# -----------------------------
def load_csv(path, sep=","):
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(path, sep=sep)

def save_csv(df, path, index=False):
    """Save a DataFrame to CSV."""
    df.to_csv(path, index=index)

# -----------------------------
# CLEANING
# -----------------------------
def clean_missing(df, strategy="drop", fill_value=None):
    """
    Handle missing values.
    strategy: 'drop', 'fill'
    """
    if strategy == "drop":
        return df.dropna()
    elif strategy == "fill":
        return df.fillna(fill_value)
    else:
        raise ValueError("Invalid strategy")

def rename_columns(df, mapping):
    """Rename columns using a dictionary."""
    return df.rename(columns=mapping)

def convert_types(df, type_map):
    """Convert column types using a dictionary."""
    return df.astype(type_map)

# -----------------------------
# FILTERING
# -----------------------------
def filter_rows(df, condition):
    """Filter rows using a boolean condition."""
    return df[condition]

def select_columns(df, cols):
    """Select specific columns."""
    return df[cols]

# -----------------------------
# GROUPING & AGGREGATION
# -----------------------------
def group_and_aggregate(df, group_cols, agg_map):
    """
    group_cols: list of columns to group by
    agg_map: dict of {column: 'mean'/'sum'/...}
    """
    return df.groupby(group_cols).agg(agg_map).reset_index()

# -----------------------------
# MERGING
# -----------------------------
def merge_dataframes(df1, df2, on, how="inner"):
    """Merge two DataFrames."""
    return pd.merge(df1, df2, on=on, how=how)

# -----------------------------
# SUMMARY STATS
# -----------------------------
def summary_stats(df):
    """Return summary statistics."""
    return df.describe()

def correlation_matrix(df):
    """Return correlation matrix."""
    return df.corr()
