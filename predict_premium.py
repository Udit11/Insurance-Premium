from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load Model and Scalers
model = joblib.load('Project 8 (Insurance Premium)/insurance_model.pkl')
scaler = joblib.load('Project 8 (Insurance Premium)/scaler.pkl')
pca = joblib.load('Project 8 (Insurance Premium)/pca.pkl')
label_encoders = joblib.load('Project 8 (Insurance Premium)/label_encoders.pkl')
feature_order = joblib.load('Project 8 (Insurance Premium)/feature_order.pkl')

# # Define Feature Order (Must match training phase)
# feature_order = ['age', 'bmi', 'children', 'gender', 'smoker', 'region', 'medical_history', 
#                  'family_medical_history', 'exercise_frequency', 'occupation', 'coverage_level']

# Categorical columns that need encoding
categorical_columns = ['gender', 'smoker', 'region', 'medical_history', 'family_medical_history',
                       'exercise_frequency', 'occupation', 'coverage_level']

# Flask App
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        
        # Ensure correct feature order and handle missing columns
        for col in feature_order:
            if col not in df.columns:
                df[col] = "Unknown"  # Default value for missing categorical columns
        df = df[feature_order]
        
        # Handle missing values in categorical columns
        df[categorical_columns] = df[categorical_columns].fillna("Unknown")
        
        # Apply pre-trained label encoders to categorical columns
        for col in categorical_columns:
            if col in label_encoders:
                encoder = label_encoders[col]
                df[col] = df[col].apply(lambda x: encoder.transform([x])[0] if x in list(encoder.classes_) else -1)
        
        df = df.fillna(df.median())
        
        # Feature Scaling & PCA
        X_scaled = scaler.transform(df)
        X_reduced = pca.transform(X_scaled)
        
        # Predict
        prediction = model.predict(X_reduced)
        predicted_premium = np.expm1(prediction)[0]  # Reverse log transformation
        
        return jsonify({'predicted_premium': predicted_premium})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)