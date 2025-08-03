

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("churn_rf_model.pkl")

st.set_page_config(page_title="Credit Card Churn Prediction", page_icon="💳")

st.title("💳 Credit Card Customer Churn Prediction")
st.write("Enter customer details below to predict whether they will stay or churn.")

# Replace with the exact feature names from your X_train.columns
feature_names = [
    'Customer_Age', 'Dependent_count', 'Months_on_book', 'Total_Relationship_Count',
    'Months_Inactive_12_mon', 'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
    'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt', 'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1',
    'Avg_Utilization_Ratio', 'Gender', 'Education_Level', 'Marital_Status',
    'Income_Category', 'Card_Category', 'Months_Since_Last_Contact'
]

# Input fields
# Define feature names
feature_names = [
    'Customer_Age', 'Dependent_count', 'Months_on_book', 'Total_Relationship_Count',
    'Months_Inactive_12_mon', 'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
    'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt', 'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1',
    'Avg_Utilization_Ratio', 'Gender', 'Education_Level', 'Marital_Status',
    'Income_Category', 'Card_Category', 'Months_Since_Last_Contact'
]

# Input fields
input_data = []

for feature in feature_names:
    if feature == "Gender":
        value = st.selectbox("Gender", ["M", "F"])
        value = 1 if value == "M" else 0  # Convert to numeric
    elif feature == "Marital_Status":
        value = st.selectbox("Marital Status", ["Married", "Single", "Divorced"])
        mapping = {"Married": 2, "Single": 1, "Divorced": 0}
        value = mapping[value]
    elif feature == "Education_Level":
        value = st.selectbox("Education Level", ["Graduate", "High School", "Post-Graduate", "Doctorate", "Uneducated"])
        mapping = {"Uneducated": 0, "High School": 1, "Graduate": 2, "Post-Graduate": 3, "Doctorate": 4}
        value = mapping[value]
    elif feature == "Income_Category":
        value = st.selectbox("Income Category", ["<40K", "40K-60K", "60K-80K", "80K-120K", "120K+"])
        mapping = {"<40K": 0, "40K-60K": 1, "60K-80K": 2, "80K-120K": 3, "120K+": 4}
        value = mapping[value]
    elif feature == "Card_Category":
        value = st.selectbox("Card Category", ["Blue", "Silver", "Gold", "Platinum"])
        mapping = {"Blue": 0, "Silver": 1, "Gold": 2, "Platinum": 3}
        value = mapping[value]
    else:
        # Numeric features
        value = st.number_input(f"{feature}:", value=0.0, step=1.0, format="%.2f")
    
    input_data.append(value)


# Prediction
if st.button("Predict Churn"):
    input_df = pd.DataFrame([input_data], columns=feature_names)
    prediction = model.predict(input_df)[0]
    if prediction == 0:
        st.success("✅ Existing Customer (Likely to Stay)")
    else:
        st.error("⚠️ Attrited Customer (Likely to Churn)")
