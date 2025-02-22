import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans 

np.random.seed(0)
X = np.random.rand(100, 2)

kmeans = KMeans(n_clusters = 3, random_state = 0)
kmeans.fit(X)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

plt.figure(figsize = (8,6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap = 'viridis', s=50, alpha = 0.6, edgecolors = 'w')

plt.scatter(centroids[:, 0], centroids[:, 1], marker ='*', color = 'red', s=200, label = 'centroids')

plt.title('K-means Clustering (K=3)', fontsize=16)
plt.xlabel('X')
plt.ylabel('Y')

plt.legend(['Data Points', 'Centroids'], loc = 'upper right')

plt.show()