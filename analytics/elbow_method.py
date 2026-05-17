from sklearn.cluster import KMeans

def elbow_method(df, max_k=10):
    inertias = []
    for k in range(1, max_k + 1):
        model = KMeans(n_clusters=k, random_state=42)
        model.fit(df)
        inertias.append(model.inertia_)
    return inertias
