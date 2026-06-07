from sklearn.metrics import silhouette_score

def compute_silhouette(df, labels):
    return silhouette_score(df, labels)
