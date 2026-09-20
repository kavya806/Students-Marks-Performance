import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model/student_performance_model.pkl")

# Page title
st.title("Student Marks Performance")
st.write("Pass-Fail Data")

st.markdown("---")

# Input fields
attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

homework = st.number_input(
    "Homework (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

midterm = st.number_input(
    "Midterm Score",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

study_hours = st.number_input(
    "Study Hours per Week",
    min_value=0.0,
    max_value=100.0,
    value=10.0
)

# Prediction button
if st.button("Predict Performance"):

    # Prepare input
    input_data = np.array([
        [attendance, homework, midterm, study_hours]
    ])

    # Make prediction
    prediction = model.predict(input_data)

    # Display result
    if prediction[0] == 1:
        st.success("Prediction: PASS")
    else:
        st.error("Prediction: FAIL")