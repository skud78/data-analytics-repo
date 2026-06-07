from data_loader import load_data
from data_cleaning import clean_dataframe
from analytics.clustering.clustering_eda import clustering_eda
from analytics.clustering.clustering import train_kmeans
from elbow_method import elbow_method
from silhouette_score import compute_silhouette

# 1. Load
df = load_data("/home/sudhir/OneDrive/prof/sw/data-analytics/ccustomers.csv")

# 2. Clean
df = clean_dataframe(df)

# 3. EDA
clustering_eda(df)

# 4. Elbow method
inertias = elbow_method(df, max_k=8)
print("Inertias:", inertias)

# 5. Train K-Means
model, labels = train_kmeans(df, n_clusters=3)
print("Cluster labels:", labels)

# 6. Silhouette score
score = compute_silhouette(df, labels)
print("Silhouette score:", score)
