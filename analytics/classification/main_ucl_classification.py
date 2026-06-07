import pandas as pd

from analytics.dataprep.data_loader import load_data
from analytics.dataprep.data_cleaning import clean_dataframe
from analytics.classification.classification import train_classifier
from analytics.evaluation import evaluate_classification

# 1. Load + clean
df = load_data("/home/sudhir/OneDrive/prof/comsci/ArtificialIntelligence/Machine Learning/sample-data/ucl_2025_26_clean.csv")
df = clean_dataframe(df)

# 2. Feature engineering
df["total_goals"] = df["home_goals"] + df["away_goals"]
df["goal_difference"] = abs(df["home_goals"] - df["away_goals"])

# 3. Create classification target
df["result"] = df.apply(
    lambda r: "home_win" if r.home_goals > r.away_goals
    else "away_win" if r.away_goals > r.home_goals
    else "draw",
    axis=1
)

# 4. Select numeric features
numeric_features = df.select_dtypes(include="number")

# 5. Combine numeric features + target
df_classification = pd.concat([numeric_features, df["result"]], axis=1)

# 6. Train classifier
model, splits = train_classifier(df_classification, target="result")

# 7. Evaluate
metrics = evaluate_classification(
    model,
    splits["X_test"],
    splits["y_test"]
)

print(metrics)
