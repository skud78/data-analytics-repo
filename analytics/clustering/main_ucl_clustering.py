from analytics.dataprep.data_loader import load_data
from analytics.dataprep.data_cleaning import clean_dataframe
from analytics.clustering.clustering import train_kmeans
from analytics.clustering.clustering_eda import clustering_eda

import pandas as pd

# 1. Load and clean
df = load_data("/home/sudhir/OneDrive/prof/comsci/ArtificialIntelligence/Machine Learning/sample-data/ucl_2025_26_clean.csv")
df = clean_dataframe(df)

# 2. Feature engineering
df["total_goals"] = df["home_goals"] + df["away_goals"]
df["goal_difference"] = abs(df["home_goals"] - df["away_goals"])

# 3. Select numeric columns
numeric_df = df.select_dtypes(include="number")

# 4. Optional EDA
clustering_eda(numeric_df)

# 5. Train clustering model
model, labels = train_kmeans(numeric_df, n_clusters=4)

# 6. Attach cluster labels
df["cluster"] = labels

print(df[["home_team","away_team","total_goals","cluster"]])
