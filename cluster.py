import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Load the Excel file
file_path = 'E:/大四第一段/數學建模比賽/支撐材料/normalized data with label.xlsx'
data = pd.read_excel(file_path)

# We will perform hierarchical clustering on the numeric columns
numeric_columns = data.columns[2:-1]  # Selecting columns from '自主创新能力' to '政策支持度'
numeric_data = data[numeric_columns]

# Calculate the linkage matrix using Ward's method
linked = linkage(numeric_data, 'ward')

# Plot the dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked,
            orientation='top',
            labels=data['证券代码'].values,
            distance_sort='descending',
            show_leaf_counts=True)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Stock Code')
plt.ylabel('Distance')
plt.show()