import pandas as pd
from sklearn.tree import DecisionTreeClassifier

from analytics.evaluation import evaluate_classification

# Fake classification dataset
df = pd.DataFrame({
    "f1": [1, 2, 3, 4],
    "f2": [1, 1, 2, 2],
    "label": ["A", "A", "B", "B"]
})

X = df[["f1", "f2"]]
y = df["label"]

model = DecisionTreeClassifier().fit(X, y)

metrics = evaluate_classification(model, X, y)
print("Classification Test:", metrics)
