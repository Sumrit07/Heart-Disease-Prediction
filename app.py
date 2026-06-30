import streamlit as st
import pandas as pd
import joblib

# ==========================
# Load Model and Files
# ==========================
model = joblib.load("SVM_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("column.pkl")

# ==========================
# Page Configuration
# ==========================
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

st.title("❤️ Heart Disease Prediction System")
st.write("Enter the patient's details below and click **Predict**.")

# ==========================
# User Inputs
# ==========================
age = st.slider("Age", 18, 100, 40)

sex = st.selectbox(
    "Sex",
    ["M", "F"]
)

chest_pain = st.selectbox(
    "Chest Pain Type",
    ["ATA", "NAP", "ASY", "TA"]
)

resting_bp = st.number_input(
    "Resting Blood Pressure",
    min_value=80,
    max_value=220,
    value=120
)

cholesterol = st.number_input(
    "Cholesterol",
    min_value=0,
    max_value=700,
    value=200
)

fasting_bs = st.selectbox(
    "Fasting Blood Sugar (>120 mg/dl)",
    [0, 1]
)

resting_ecg = st.selectbox(
    "Resting ECG",
    ["Normal", "ST", "LVH"]
)

max_hr = st.slider(
    "Maximum Heart Rate",
    60,
    220,
    150
)

exercise_angina = st.selectbox(
    "Exercise Induced Angina",
    ["Y", "N"]
)

oldpeak = st.slider(
    "Oldpeak",
    0.0,
    6.5,
    1.0
)

st_slope = st.selectbox(
    "ST Slope",
    ["Up", "Flat", "Down"]
)

# ==========================
# Prediction
# ==========================
if st.button("Predict"):

    # Initialize all columns with 0
    input_dict = {col: 0 for col in expected_columns}

    # Numerical Features
    if "Age" in input_dict:
        input_dict["Age"] = age

    if "RestingBP" in input_dict:
        input_dict["RestingBP"] = resting_bp

    if "Cholesterol" in input_dict:
        input_dict["Cholesterol"] = cholesterol

    if "FastingBS" in input_dict:
        input_dict["FastingBS"] = fasting_bs

    if "MaxHR" in input_dict:
        input_dict["MaxHR"] = max_hr

    if "Oldpeak" in input_dict:
        input_dict["Oldpeak"] = oldpeak

    # One-Hot Encoded Features
    if f"Sex_{sex}" in input_dict:
        input_dict[f"Sex_{sex}"] = 1

    if f"ChestPainType_{chest_pain}" in input_dict:
        input_dict[f"ChestPainType_{chest_pain}"] = 1

    if f"RestingECG_{resting_ecg}" in input_dict:
        input_dict[f"RestingECG_{resting_ecg}"] = 1

    if f"ExerciseAngina_{exercise_angina}" in input_dict:
        input_dict[f"ExerciseAngina_{exercise_angina}"] = 1

    if f"ST_Slope_{st_slope}" in input_dict:
        input_dict[f"ST_Slope_{st_slope}"] = 1

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Ensure column order
    input_df = input_df[expected_columns]

    # Scale
    scaled_input = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(scaled_input)[0]

    # Probability (if supported)
    probability = None
    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(scaled_input)[0][1]

    st.divider()

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")

    if probability is not None:
        st.write(f"Prediction Confidence: **{probability:.2%}**")

    st.subheader("Input Summary")

    st.dataframe(input_df)