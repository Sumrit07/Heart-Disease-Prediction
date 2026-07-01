# ❤️ Heart Disease Prediction System

## Project Overview

Heart disease is one of the leading causes of death worldwide. Early prediction can help in timely diagnosis and treatment. This project develops a Machine Learning-based Heart Disease Prediction System using a Support Vector Machine (SVM) classifier. The application is deployed using Streamlit, allowing users to enter patient health information and instantly receive a prediction.

The project demonstrates how Machine Learning and data preprocessing techniques can be combined to build an interactive healthcare prediction application.


🌐 Live Demo / Deployment

 ## 👉 Streamlit App: https://heart-disease-prediction-mbuuxbhesyr4w7fpwymgwg.streamlit.app/
---

## Project Objectives

- Predict the likelihood of heart disease using patient health data.
- Build an interactive web application using Streamlit.
- Apply data preprocessing techniques for accurate predictions.
- Encode categorical features using One-Hot Encoding.
- Scale numerical features using StandardScaler.
- Deploy a trained Machine Learning model for real-time prediction.

---

## Dataset Information

The dataset contains patient medical records with features such as:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- Oldpeak
- ST Slope
- Heart Disease (Target)

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## Project Workflow

1. Data Loading
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. One-Hot Encoding
5. Feature Scaling
6. Model Training using Support Vector Machine (SVM)
7. Model Evaluation
8. Model Serialization using Joblib
9. Streamlit Application Development
10. Deployment

---

## Features

- Interactive Streamlit User Interface
- Real-Time Heart Disease Prediction
- Automatic Feature Encoding
- Standardized Input Scaling
- Fast Prediction using Trained SVM Model
- Displays Prediction Summary

---

## Machine Learning Model

- Algorithm: Support Vector Machine (SVM)
- Feature Scaling: StandardScaler
- Encoding: One-Hot Encoding
- Model Persistence: Joblib

---

## How to Run the Project

### Clone the repository

```bash
git clone https://github.com/Sumrit07/Heart-Disease-Prediction.git
```

### Navigate to the project folder

```bash
cd Heart-Disease-Prediction
```

### Install the required libraries

```bash
pip install -r requirements.txt
```

### Run the Streamlit Application

```bash
streamlit run app.py
```

---

## Project Structure

```
Heart-Disease-Prediction/
│
├── app.py
├── SVM_heart.pkl
├── scaler.pkl
├── column.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Future Scope

This project can be extended by:

- Deploying using Docker
- Adding multiple Machine Learning models for comparison
- Displaying prediction probability and confidence score
- Integrating with cloud databases
- Providing downloadable medical reports
- Improving UI with advanced visualizations

---

## Conclusion

This project demonstrates how Machine Learning can assist in predicting the risk of heart disease using patient health information. By combining data preprocessing, feature engineering, and an SVM classifier with an interactive Streamlit interface, the application provides quick and reliable predictions that can support healthcare decision-making.

---

## Author

Sumrit Singh Chouhan
