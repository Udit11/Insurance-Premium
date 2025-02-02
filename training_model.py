import sqlite3
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
# from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import joblib

# Load Data
conn = sqlite3.connect('Database.db')
data = pd.read_sql_query('SELECT * FROM Insurance_Prediction', conn)
conn.close()

# Data Preprocessing
data['age'] = pd.to_numeric(data['age'], errors='coerce')
data['bmi'] = pd.to_numeric(data['bmi'], errors='coerce')
data['children'] = pd.to_numeric(data['children'], errors='coerce')
data['charges'] = pd.to_numeric(data['charges'], errors='coerce')

# Label Encoding for Categorical Variables
label_encoder = {}
categorical_columns = ['gender', 'smoker', 'region', 'medical_history', 'family_medical_history', 'exercise_frequency', 'occupation', 'coverage_level']
for col in categorical_columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col].astype(str))
    label_encoder[col] = le

# Handling Missing Values
data.fillna(data.median(), inplace=True)

# Handling Outliers using IQR
def handle_outliers_iqr(df, col):
    Q1, Q3 = df[col].quantile([0.25, 0.75])
    IQR = Q3 - Q1
    lower_bound, upper_bound = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
    df[col] = np.clip(df[col], lower_bound, upper_bound)

for col in ['age', 'bmi', 'children', 'charges']:
    handle_outliers_iqr(data, col)

data['charges'] = np.log1p(data['charges'])  # Log transformation

# Feature Scaling & PCA
X = data.drop(columns=['charges'])
y = data['charges']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=10)
X_reduced = pca.fit_transform(X_scaled)

feature_order = X.columns.tolist()

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_reduced, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestRegressor()
# model = DecisionTreeRegressor(random_state=0)
model.fit(X_train, y_train)

# Save Model & Scaler
joblib.dump(model, 'Project 8 (Insurance Premium)/insurance_model.pkl')
joblib.dump(scaler, 'Project 8 (Insurance Premium)/scaler.pkl')
joblib.dump(pca, 'Project 8 (Insurance Premium)/pca.pkl')
joblib.dump(label_encoder, 'Project 8 (Insurance Premium)/label_encoders.pkl')
joblib.dump(feature_order, 'Project 8 (Insurance Premium)/feature_order.pkl')

print("Model training complete. Model saved as insurance_model.pkl")
