import streamlit as st
import pickle 
import numpy as np


# Load your trained model
model = pickle.load(open(r'D:\ICBT Lecs\CI\ci\insurance_model.pkl', 'rb'))

# Create the user interface
st.title("Insurance Response Prediction")
st.write("Enter the details below to predict customer response to insurance offer:")

# Add input fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)
gender = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
vehicle_age = st.selectbox("Vehicle Age", options=[1, 2, 3], format_func=lambda x: "< 1 Year" if x == 1 else "1-2 Year" if x == 2 else "> 2 Years")
vehicle_damage = st.selectbox("Vehicle Damage", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
annual_premium = st.number_input("Annual Premium", min_value=0, max_value=500000, value=10000)
policy_sales_channel = st.number_input("Policy Sales Channel", min_value=1, max_value=200, value=1)
vintage = st.number_input("Vintage", min_value=0, max_value=300, value=100)


# Make prediction
if st.button("Predict"):
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        st.success("The customer is likely to respond positively to the insurance offer.")
    else:
        st.warning("The customer is likely to decline the insurance offer.")

