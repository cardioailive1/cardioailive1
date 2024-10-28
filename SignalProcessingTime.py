#1.  Import Libraries....
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import time

# 2.  Simulate signal data (example: 1000 samples of 10 features each)
np.random.seed(42)
X = np.random.rand(1000, 10)  # Features (e.g., time-series signal data)
y = np.random.randint(0, 2, 1000)  # Binary target (0 or 1)

# 3.  Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4.  Create a pipeline: scaler (optional) and classifier
scaler = StandardScaler()
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# 5.  Scale the data
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6.  Train the classifier
clf.fit(X_train_scaled, y_train)

# 7.  Predict and time the processing
start_time = time.time()
y_pred = clf.predict(X_test_scaled)
processing_time = time.time() - start_time

# 8.  Print results
print(f"Prediction Time: {processing_time:.4f} seconds")
if processing_time <= 2:
    print("The processing time is within the 2-second limit.")
else:
    print("The processing time exceeds the 2-second limit.")

# 9. Evaluate the model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred))
