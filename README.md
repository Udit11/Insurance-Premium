# Insurance Premium Prediction API

## Overview
The **Insurance Premium Prediction API** is a robust Flask-based application designed to predict health insurance premiums based on user-provided data. The API leverages machine learning models to deliver accurate, real-time predictions by processing input features such as age, gender, BMI, and medical history. The project includes scripts for data preprocessing, model training, and a RESTful API endpoint for seamless integration into applications.

This repository provides a complete solution, including model training, data persistence with SQLite, and a production-ready API for real-time predictions.

---

## Project Structure
```
Insurance-Premium-Prediction/
│
├── training_model.py         # Script for data preprocessing and model training
├── predict_premium.py        # Flask API for real-time premium predictions
├── Database.db               # SQLite database storing insurance data
├── README.md                 # Project documentation (this file)
├── insurance_model.pkl       # Trained machine learning model
├── scaler.pkl                # StandardScaler for feature normalization
├── pca.pkl                   # PCA model for dimensionality reduction
├── label_encoders.pkl        # Dictionary of LabelEncoder objects for categorical features
├── feature_order.pkl         # List of feature names to ensure input consistency
```

---

## Setup Instructions

### Prerequisites
- **Python 3.8+**: Ensure Python is installed on your system.
- **pip**: Python package manager for installing dependencies.

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Insurance-Premium-Prediction.git
   cd Insurance-Premium-Prediction
   ```

2. **Install Dependencies**:
   Install the required Python libraries using pip:
   ```bash
   pip install flask pandas scikit-learn joblib numpy
   ```

3. **Train the Model**:
   Execute the training script to preprocess the data, train the model, and save the artifacts (`insurance_model.pkl`, `scaler.pkl`, `pca.pkl`, `label_encoders.pkl`, `feature_order.pkl`):
   ```bash
   python training_model.py
   ```

4. **Run the Flask API**:
   Start the Flask server to deploy the prediction API:
   ```bash
   python predict_premium.py
   ```
   The API will be accessible at:
   ```
   http://127.0.0.1:5000/predict
   ```

---

## Using the API

### Endpoint
- **URL**: `http://127.0.0.1:5000/predict`
- **Method**: `POST`
- **Content-Type**: `application/json`

### Request Format
Send a JSON payload with the following structure:
```json
{
    "age": 35,
    "gender": "male",
    "bmi": 27.5,
    "children": 2,
    "smoker": "no",
    "region": "southwest",
    "medical_history": "None",
    "family_medical_history": "Diabetes",
    "exercise_frequency": "Regular",
    "occupation": "Blue collar",
    "coverage_level": "Premium"
}
```

### Response Format
The API returns a JSON response with the predicted insurance premium:
```json
{
    "predicted_premium": 14560.89
}
```

### Example Request (Using `curl`)
```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"age": 35, "gender": "male", "bmi": 27.5, "children": 2, "smoker": "no", "region": "southwest", "medical_history": "None", "family_medical_history": "Diabetes", "exercise_frequency": "Regular", "occupation": "Blue collar", "coverage_level": "Premium"}'
```

---

## Troubleshooting

### 1. Feature Mismatch Error
**Error**: `"The feature names should match those that were passed during fit."`
**Solution**: Ensure that `feature_order.pkl` is correctly loaded and used in `predict_premium.py` to align input features with the trained model.

### 2. Label Encoding Error
**Error**: `"argument of type 'LabelEncoder' is not iterable"`
**Solution**: Verify that `training_model.py` saves the `LabelEncoder` objects as a dictionary in `label_encoders.pkl` and that it is properly loaded in `predict_premium.py`.

### 3. API Not Responding
**Solution**:
- Ensure the Flask server is running (`python predict_premium.py`).
- Check that the correct port (`5000`) is open and not blocked by a firewall.
- Validate the JSON payload for missing or incorrect fields.

---

## Technologies Used
- **Python**: Core programming language
- **Flask**: Web framework for the API
- **Scikit-learn**: Machine learning library for model training
- **Pandas**: Data manipulation and preprocessing
- **NumPy**: Numerical computations
- **SQLite**: Lightweight database for storing insurance data
- **Joblib**: Model serialization and deserialization

---

## Authors
- **Developed by**: Udit Srivastava
- **Contact**: [uditsrivastava2347@gmail.com](mailto:uditsrivastava2347@gmail.com)
- **GitHub**: https://github.com/Udit11

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Download
This `README.md` can be downloaded as a standalone file for reference:
[Download README.md](https://raw.githubusercontent.com/your-username/Insurance-Premium-Prediction/main/README.md)
