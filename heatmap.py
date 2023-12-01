import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'E:/大四第一段/數學建模比賽/支撐材料/normalized data with label.xlsx'
data = pd.read_excel(file_path)

# Select only the columns with the features, ordered as specified
features_ordered = ['政策支持度', '自主創新能力', '系統性風險度', '市場重估度', '社會責任度']

# Calculate the correlation matrix
correlation_matrix = data[features_ordered].corr()

# English labels for the features, in the order specified
feature_names_english_ordered = ['Policy Support', 'Innovation Capability', 'Systemic Risk', 'Market Revaluation', 'Social Responsibility']

# Rename the columns and index of the correlation matrix to English
correlation_matrix_english = correlation_matrix.rename(columns=dict(zip(features_ordered, feature_names_english_ordered)), 
                                                       index=dict(zip(features_ordered, feature_names_english_ordered)))

# Plot the heatmap with English labels
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix_english, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
plt.title('Feature Correlation Heatmap')
plt.show()
