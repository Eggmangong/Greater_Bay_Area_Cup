""" 任务一 SVM训练代码"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, accuracy_score

# Load the data
file_path = 'E:/大四第一段/數學建模比賽/支撐材料/unnormalized data with label.xlsx'
data = pd.read_excel(file_path)

# Separate features and target variable
X = data.iloc[:, 2:-1]  # Exclude the first two columns and the last column
y = data.iloc[:, -1]  # Target variable is the last column

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize a pipeline with Standard Scaler and SVM with a linear kernel
# We use class_weight='balanced' to address the class imbalance issue
pipeline = make_pipeline(StandardScaler(), SVC(kernel='linear', class_weight='balanced'))

# Train the SVM model
pipeline.fit(X_train, y_train)

# Predict on the test set
y_pred = pipeline.predict(X_test)

# Calculate accuracy and classification report
accuracy = accuracy_score(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Output the results
print(f'Accuracy: {accuracy}')
print(f'Classification Report: \n{class_report}')

# Retrieve the SVM model from the pipeline
svm_model = pipeline.named_steps['svc']

# Get the weights of the features
feature_weights = svm_model.coef_[0]
# Get the bias term from the SVM model
bias = svm_model.intercept_[0]

# Display the weights and bias
weights_df = pd.DataFrame({'Feature': X.columns, 'Weight': feature_weights})
print(weights_df)
print(f'Bias: {bias}')
