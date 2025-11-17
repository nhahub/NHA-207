import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib # To save the model

# --- 1. Load the Prepared Data ---
# Ensure this path is correct based on where you saved the output
df_ml = pd.read_csv('../data/clean/ml_data_for_prediction.csv')

print("1. Data Loaded. Shape:", df_ml.shape)

# --- 2. Separate Features (X) and Target (Y) ---
# Drop non-predictive columns (names, IDs, etc.)
columns_to_drop = [
    'employeeid', 'firstname', 'lastname', 'hiredate', 
    'education_level_text', # Text version of Education is redundant
    'avg_rating_change' # Optional: Can be complex, let's simplify for the first run
]
df_ml.drop(columns=columns_to_drop, inplace=True, errors='ignore')

# Target Variable
Y = df_ml['attrition_binary']
# Features
X = df_ml.drop('attrition_binary', axis=1)

# --- 3. One-Hot Encoding for Remaining Categorical Variables ---
# Identify categorical columns (object type)
categorical_cols = X.select_dtypes(include=['object']).columns

# Perform One-Hot Encoding (creates new binary columns for each category)
X_encoded = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

# Fill any remaining NaNs (e.g., from the new lag features) with the median
X_encoded.fillna(X_encoded.median(), inplace=True)

print("2. Features Encoded and NaNs Handled. New Shape:", X_encoded.shape)

# --- 4. Split Data into Training and Testing Sets ---
# We use a 70/30 split, stratify to ensure the rare 'Attrition=1' is balanced
X_train, X_test, Y_train, Y_test = train_test_split(
    X_encoded, 
    Y, 
    test_size=0.3, 
    random_state=42,
    stratify=Y # Crucial for unbalanced classification tasks
)

print("3. Data Split: Training Size:", X_train.shape[0], "Testing Size:", X_test.shape[0])

# --- 5. Train the Model (Random Forest Classifier) ---
# Random Forest is a great default model for HR data
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, Y_train)

print("4. Model Training Complete.")

# --- 6. Evaluate the Model ---
Y_pred = model.predict(X_test)
Y_proba = model.predict_proba(X_test)[:, 1] # Probability of attrition (Class 1)

print("\n--- Model Evaluation ---")
print("Accuracy:", accuracy_score(Y_test, Y_pred))
print("\nClassification Report:\n", classification_report(Y_test, Y_pred))

# --- 7. Generate Final Predictions on the ENTIRE Dataset ---
# Use the full encoded dataset (X_encoded) to predict probabilities for ALL employees
final_probabilities = model.predict_proba(X_encoded)[:, 1]

# --- 8. Create and Export the Prediction File ---
# We need the original IDs for merging back into Power BI
df_predictions = pd.DataFrame({
    'employeeid': pd.read_csv('../data/clean/ml_data_for_prediction.csv')['employeeid'],
    'prediction_score': final_probabilities
})

# Save the trained model for later use (optional but recommended)
joblib.dump(model, '../models/random_forest_model.pkl')
print("\nModel saved to '../models/random_forest_model.pkl'")

# Save the predictions file for Power BI
df_predictions.to_csv('../data/clean/employee_predictions.csv', index=False)
print("5. ✅ Exported: employee_predictions.csv (Ready for Power BI)")