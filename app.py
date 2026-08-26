import streamlit as st

st.set_page_config(page_title="AI Loan Fraud Risk Detector")

st.title("AI Loan Fraud Risk Detector")

st.write("Predict the risk level of a loan applicant.")

income = st.number_input("Monthly Income", min_value=0)

credit_score = st.number_input("Credit Score", min_value=0, max_value=900)

loan_amount = st.number_input("Loan Amount", min_value=0)

if st.button("Predict Risk"):

    if credit_score >= 750 and income >= 50000:
        risk = "Low Risk"

    elif credit_score >= 600:
        risk = "Medium Risk"

    else:
        risk = "High Risk"

    st.success(f"Predicted Risk Level: {risk}")
