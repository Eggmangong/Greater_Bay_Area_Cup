import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.metrics import pairwise_distances
import matplotlib.pyplot as plt
import numpy as np

# Load the Excel file
file_path = 'E:\\大四第一段\\數學建模比賽\\支撐材料\\normalized data only csi.xlsx'
data = pd.read_excel(file_path)

# Selecting relevant columns for clustering (excluding '证券代码' and '证券名称')
clustering_data = data.iloc[:, 2:]

# Using the hierarchical clustering method
linked = linkage(clustering_data, method='ward')

# Creating a dendrogram to visualize the hierarchical clustering
plt.figure(figsize=(10, 7.5))
dendrogram(linked, orientation='top', labels=data['证券代码'].values, distance_sort='descending', show_leaf_counts=True, color_threshold=8)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Stock Code')
plt.ylabel('Distance')
plt.show()

# Function to calculate the total within-cluster sum of square (WSS)
def calculate_wss(points, kmax):
    sse = []
    for k in range(1, kmax+1):
        # Determine the clusters at the given level k
        labels = fcluster(linked, k, criterion='maxclust')
        # Calculate pairwise distance matrix for the dataset
        dist_matrix = pairwise_distances(points)
        # Sum of squares within each cluster
        total_within_ss = 0
        for i in range(1, k+1):
            cluster_points = points[labels == i]
            if cluster_points.shape[0] > 0:  # Check if the cluster is not empty
                cluster_distance_matrix = pairwise_distances(cluster_points)
                total_within_ss += np.sum(cluster_distance_matrix**2)
        sse.append(total_within_ss)
    return sse

# Calculate WSS for a range of number of clusters
kmax = 10  # maximum number of clusters to consider
wss = calculate_wss(clustering_data, kmax)

# Plot the Elbow Method Graph
plt.figure(figsize=(8, 6))
plt.plot(range(1, kmax+1), wss, marker='o')
plt.title('Elbow Method For Optimal k')
plt.xlabel('Number of clusters')
plt.ylabel('Total within-cluster sum of squares')
plt.xticks(range(1, kmax+1))
plt.show()