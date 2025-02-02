# Insurance Premium Prediction API

## 📌 Overview
This project provides a **Flask API** for predicting health insurance premiums based on user details.  
It includes **data preprocessing, model training, and a real-time prediction endpoint**.

---

## 📁 Project Structure
# Insurance Premium Prediction API

## 📌 Overview
This project provides a **Flask API** for predicting health insurance premiums based on user details.  
It includes **data preprocessing, model training, and a real-time prediction endpoint**.

---

## 📁 Project Structure
Project 8 (Insurance Premium)/ │── training_model.py # Script for training and saving the model │── predict_premium.py # Flask API for real-time predictions │── Database.db # SQLite database with insurance data │── README.md # Documentation (this file) │── insurance_model.pkl # Saved trained model │── scaler.pkl # StandardScaler for data normalization │── pca.pkl # PCA model for dimensionality reduction │── label_encoders.pkl # Dictionary of trained LabelEncoders │── feature_order.pkl # List of feature names for consistency


---

## ⚙️ **Setup Instructions**
### **1️⃣ Install Dependencies**
Ensure you have Python 3 installed. Then install required libraries:
```bash
pip install flask pandas scikit-learn joblib numpy

2️⃣ Train the Model
Run training_model.py to process the data, train the model, and save all required files.
python training_model.py

3️⃣ Start the Flask API
Run predict_premium.py to start the API:
python predict_premium.py

The API will run at:
🔗 http://127.0.0.1:5000/predict

🚀 Using the API
1️⃣ Request Format (JSON)
Send a POST request to http://127.0.0.1:5000/predict with the following JSON:

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

2️⃣ Response Format
{
    "predicted_premium": 14560.89
}

❗ Troubleshooting
1️⃣ Feature Mismatch Error
Error: "The feature names should match those that were passed during fit."
✔️ Fix: Ensure feature_order.pkl is used correctly in predict_premium.py.

2️⃣ Label Encoding Error
Error: "argument of type 'LabelEncoder' is not iterable"
✔️ Fix: Ensure training_model.py properly saves label encoders as a dictionary.


I can't directly provide a download button, but you can manually download the file by following these steps:

Copy the content below and save it as README.md on your local machine.
If you're using a terminal, you can create it using:
bash
Copy
Edit
nano README.md
Then paste the content and save it.
README.md
markdown
Copy
Edit
# Insurance Premium Prediction API

## 📌 Overview
This project provides a **Flask API** for predicting health insurance premiums based on user details.  
It includes **data preprocessing, model training, and a real-time prediction endpoint**.

---

## 📁 Project Structure
Project 8 (Insurance Premium)/ │── training_model.py # Script for training and saving the model │── predict_premium.py # Flask API for real-time predictions │── Database.db # SQLite database with insurance data │── README.md # Documentation (this file) │── insurance_model.pkl # Saved trained model │── scaler.pkl # StandardScaler for data normalization │── pca.pkl # PCA model for dimensionality reduction │── label_encoders.pkl # Dictionary of trained LabelEncoders │── feature_order.pkl # List of feature names for consistency

yaml
Copy
Edit

---

## ⚙️ **Setup Instructions**
### **1️⃣ Install Dependencies**
Ensure you have Python 3 installed. Then install required libraries:
```bash
pip install flask pandas scikit-learn joblib numpy
2️⃣ Train the Model
Run training_model.py to process the data, train the model, and save all required files.

bash
Copy
Edit
python training_model.py
3️⃣ Start the Flask API
Run predict_premium.py to start the API:

bash
Copy
Edit
python predict_premium.py
The API will run at:
🔗 http://127.0.0.1:5000/predict

🚀 Using the API
1️⃣ Request Format (JSON)
Send a POST request to http://127.0.0.1:5000/predict with the following JSON:

json
Copy
Edit
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
2️⃣ Response Format
json
Copy
Edit
{
    "predicted_premium": 14560.89
}
❗ Troubleshooting
1️⃣ Feature Mismatch Error
Error: "The feature names should match those that were passed during fit."
✔️ Fix: Ensure feature_order.pkl is used correctly in predict_premium.py.

2️⃣ Label Encoding Error
Error: "argument of type 'LabelEncoder' is not iterable"
✔️ Fix: Ensure training_model.py properly saves label encoders as a dictionary.

📝 Authors
Developed by: Udit Srivastava
Technologies Used: Python, Flask, Scikit-learn, Pandas, SQLite


---

Let me know if you need any modifications! 🚀
