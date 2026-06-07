from sklearn.cluster import KMeans

def train_kmeans(df, n_clusters=3):
    model = KMeans(n_clusters=n_clusters, random_state=42)
    model.fit(df)
    labels = model.labels_
    return model, labels
