
# F1 Score for Classification Task
#      Current F1-Score : 0.75 - 0.85 & we need >=0.90

#- to improve F1 Score, 
#    focus on improving data quality, balancing classes, 
#    hyperparameter tuning, and potentially switching to more complex or 
#    ensemble models. Carefully adjust the decision threshold, 
#    use cross-validation, and focus on metrics (like F1 score) that 
#    align with your specific goals.

# Error Rate for Integrated output | error rate: 10-15% | eror rate < 5% for diagnostic outputs



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 1. import library
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, classification_report
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

#2. Generate a synthetic dataset (replace this with your actual data)
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, weights=[0.7, 0.3], random_state=42)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#4. Use SMOTE for oversampling minority class (to balance the dataset)
smote = SMOTE(random_state=42)

#5.  Define the RandomForestClassifier model
rf = RandomForestClassifier(random_state=42)

#6.  Set up a pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Feature scaling
    ('smote', smote),              # Handle class imbalance
    ('rf', rf)                     # Classification model
])

#7. Define parameter grid for RandomizedSearchCV
param_dist = {
    'rf__n_estimators': [100, 200, 300],
    'rf__max_depth': [10, 20, 30, None],
    'rf__min_samples_split': [2, 5, 10],
    'rf__min_samples_leaf': [1, 2, 4],
    'rf__bootstrap': [True, False],
    'rf__class_weight': ['balanced', 'balanced_subsample', None]  # Handle imbalance
}

#8. Use RandomizedSearchCV to find the best hyperparameters
random_search = RandomizedSearchCV(pipeline, param_distributions=param_dist, 
                                   n_iter=20, scoring='f1', cv=5, verbose=1, n_jobs=-1, random_state=42)

#9.  Train the model with hyperparameter tuning
random_search.fit(X_train, y_train)

#10. Predict on test set
y_pred = random_search.predict(X_test)

# Calculate F1 score
f1 = f1_score(y_test, y_pred)

#11. Print the F1 score and classification report
print(f'Best F1 Score (Training): {random_search.best_score_}')
print(f'F1 Score (Test): {f1}')
print("Classification Report:\n", classification_report(y_test, y_pred))

#12. Print best parameters
print("Best Parameters:\n", random_search.best_params_)


#13.  Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)

#14.  Calculate Error Rate
error_rate = 1 - accuracy

#15.  Print the accuracy, and error rate

print(f'Accuracy (Test): {accuracy * 100:.2f}%')
print(f'Error Rate (Test): {error_rate * 100:.2f}%')


#16.  Check if error rate is below the target of 5%
if error_rate < 0.05:
    print("Success! The model has achieved the target error rate of less than 5%.")
else:
    print("The error rate is still above 5%. Further optimization may be needed.")
