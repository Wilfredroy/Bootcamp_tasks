import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

n_samples = 300
n_features = 2
n_clusters = 3

X, _ = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, cluster_std=0.60, random_state=0)


plt.scatter(X[:, 0], X[:, 1], s=30, cmap='viridis')
plt.title("Generated Dataset")
plt.show()

kmeans_runs = 5 
n_clusters = 3  

plt.figure(figsize=(15, 12))

for i in range(kmeans_runs):
    kmeans = KMeans(n_clusters=n_clusters, init='random', n_init=1, random_state=i)
    kmeans.fit(X)
    
    plt.subplot(2, 3, i+1)  
    plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, s=30, cmap='viridis') 
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', s=200, alpha=0.75, marker='X') 
    plt.title(f"K-means Run {i+1}")
    
plt.tight_layout()
plt.show()
