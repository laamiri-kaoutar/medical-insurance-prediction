import streamlit as st
import joblib
import numpy as np

# Load your trained model (replace with your filename)
model = joblib.load("xgb_model_joblib")

# Title of the app
st.title("Medical Charges Prediction App")

st.write("Enter the patient information below and get an estimated charge:")

# Example input fields (we’ll add more later)
age = st.number_input("Age", min_value=0, max_value=120, value=25)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
sex = st.selectbox("Sex", ["male", "female"])
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker?", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

import pandas as pd

if st.button("Predict Charges"):
    input_data = pd.DataFrame([{
        "age": age,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region,
        "sex": sex
    }])

    log_prediction = model.predict(input_data)
    prediction = np.exp(log_prediction)

    st.success(f"Estimated Medical Charges: ${prediction[0]:,.2f}")
