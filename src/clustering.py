from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import silhouette_score
import numpy as np
import pandas as pd

def create_clusters(df, sample_size=50000, k_min=2, k_max=10, pca_variance=0.98):
    """
    Strong clustering for large datasets
    - df: input DataFrame
    - sample_size: number of rows for silhouette scoring
    - k_min, k_max: range of clusters to try
    - pca_variance: variance to keep in PCA (0-1)
    """
    print("🔍 Preparing and transforming data...")

    # Features to use
    features = ['price', 'load', 'rating', 'reviews', 'rank']
    X = df[features].fillna(0).copy()

    # Log-transform skewed numeric features
    for col in ['price', 'load', 'reviews']:
        X[col] = X[col].apply(lambda x: np.log1p(x))  # log(1+x) to handle 0

    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Dimensionality reduction with PCA
    pca = PCA(n_components=pca_variance, random_state=42)
    X_reduced = pca.fit_transform(X_scaled)
    print(f"🔹 Reduced to {X_reduced.shape[1]} dimensions using PCA")

    # Take a random sample for silhouette scoring
    if X_reduced.shape[0] > sample_size:
        idx = np.random.choice(X_reduced.shape[0], sample_size, replace=False)
        X_sample = X_reduced[idx]
    else:
        X_sample = X_reduced

    print("🚀 Finding best number of clusters...")
    best_k = k_min
    best_score = -1

    for k in range(k_min, k_max + 1):
        model = MiniBatchKMeans(n_clusters=k, batch_size=10000, random_state=42)
        labels = model.fit_predict(X_sample)
        score = silhouette_score(X_sample, labels)
        print(f"k={k}, silhouette_score={score:.4f}")
        if score > best_score:
            best_score = score
            best_k = k

    print(f"✅ Best k found: {best_k}")

    # Fit final model on full dataset
    print("🎯 Fitting final model on full dataset...")
    final_model = MiniBatchKMeans(n_clusters=best_k, batch_size=10000, random_state=42)
    df['cluster'] = final_model.fit_predict(X_reduced)

    print("✅ Strong clustering done!")
    return df
#More mathematically correct
#Finds “best k” using full data
#Good for small datasets

#Extremely slow on 862K rows
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans
# from sklearn.metrics import silhouette_score
# import numpy as np

# def create_clusters(df):
#     print("🔍 Creating clusters...")

#     features = ['price', 'load', 'rating', 'reviews', 'rank']
#     X = df[features].fillna(0)

#     scaler = StandardScaler()
#     X_scaled = scaler.fit_transform(X)

#     # 🔥 Find best K automatically
#     best_k = 2
#     best_score = -1

#     for k in range(2, 10):
#         model = KMeans(n_clusters=k, random_state=42, n_init=10)
#         labels = model.fit_predict(X_scaled)

#         score = silhouette_score(X_scaled, labels)

#         if score > best_score:
#             best_score = score
#             best_k = k

#     print(f"✅ Best clusters: {best_k}")

#     final_model = KMeans(n_clusters=best_k, random_state=42, n_init=10)
#     df['cluster'] = final_model.fit_predict(X_scaled)

#     print("✅ Clustering Done")
#     return df
