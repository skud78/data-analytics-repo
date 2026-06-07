import pandas as pd
from sklearn.cluster import KMeans

from analytics.evaluation import evaluate_clustering

# Fake clustering dataset
df = pd.DataFrame({
    "f1": [1, 2, 3, 8, 9, 10],
    "f2": [1, 2, 3, 8, 9, 10]
})

# Train a simple KMeans model
model = KMeans(n_clusters=2, n_init=10)
labels = model.fit_predict(df)

# Evaluate clustering
metrics = evaluate_clustering(df, labels)
print("Clustering Test:", metrics)
