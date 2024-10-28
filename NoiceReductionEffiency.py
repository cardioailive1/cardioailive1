# 1. Import Libraries

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Simulate ECG signal data (or load real ECG dataset)
# Example: 5000 samples, each with 1000 time points
np.random.seed(42)
X = np.random.randn(5000, 1000)  # Simulated ECG signals with noise
y = np.random.randint(0, 2, 5000)  # Binary labels: 0 for low noise, 1 for high noise

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Evaluate the model
y_pred = rf_model.predict(X_test)

# Print accuracy and classification report
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred))

# Assessing Noise Reduction Efficiency
noise_reduction_efficiency = accuracy * 100
print(f"Noise Reduction Efficiency: {noise_reduction_efficiency:.2f}%")
