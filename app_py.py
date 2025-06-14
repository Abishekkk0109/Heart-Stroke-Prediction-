# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dpWjyGD6tWTj5U9R9BKeFAznfpXlpAAf
"""

import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("/content/xgboost_stroke_model.pkl")

# Title
st.title("🧠 Heart Stroke Prediction App")
st.write("Enter patient details below to predict the likelihood of stroke.")

# Input fields
gender = st.selectbox("Gender", ['Male', 'Female', 'Other'])
ever_married = st.selectbox("Ever Married?", ['Yes', 'No'])
work_type = st.selectbox("Work Type", ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
residence_type = st.selectbox("Residence Type", ['Urban', 'Rural'])
smoking_status = st.selectbox("Smoking Status", ['never smoked', 'formerly smoked', 'smokes', 'Unknown'])

age = st.slider("Age", 1, 100, 30)
avg_glucose_level = st.slider("Average Glucose Level", 50.0, 300.0, 100.0)
bmi = st.slider("BMI", 10.0, 60.0, 22.0)
hypertension = st.selectbox("Hypertension", ['No', 'Yes'])
heart_disease = st.selectbox("Heart Disease", ['No', 'Yes'])

# Preprocess inputs
def preprocess_input():
    gender_Male = 1 if gender == "Male" else 0
    gender_Other = 1 if gender == "Other" else 0
    ever_married_Yes = 1 if ever_married == "Yes" else 0
    work_type_dict = {'Private': [1, 0, 0, 0], 'Self-employed': [0, 1, 0, 0], 'Govt_job': [0, 0, 1, 0],
                      'children': [0, 0, 0, 1], 'Never_worked': [0, 0, 0, 0]}
    work_type_encoded = work_type_dict[work_type]
    residence_type_Urban = 1 if residence_type == "Urban" else 0
    smoking_dict = {'never smoked': [0, 0, 0], 'formerly smoked': [1, 0, 0], 'smokes': [0, 1, 0], 'Unknown': [0, 0, 1]}
    smoking_encoded = smoking_dict[smoking_status]
    hypertension = 1 if hypertension == "Yes" else 0
    heart_disease = 1 if heart_disease == "Yes" else 0

    input_data = [age, avg_glucose_level, bmi, hypertension, heart_disease,
                  gender_Male, gender_Other, ever_married_Yes,
                  *work_type_encoded, residence_type_Urban, *smoking_encoded]
    return np.array(input_data).reshape(1, -1)

# Predict
if st.button("Predict Stroke"):
    input_array = preprocess_input()
    prediction = model.predict(input_array)[0]
    probability = model.predict_proba(input_array)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High risk of stroke! (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Low risk of stroke. (Probability: {probability:.2f})")

!streamlit run app_py.py

