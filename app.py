import streamlit as st

st.set_page_config(page_title="AI Loan Fraud Risk Detector")

st.title("🏦 AI Loan Fraud Risk Detector")

st.write("Enter applicant details to predict risk level.")

income = st.number_input("Monthly Income (₹)", min_value=0)

credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=900
)

loan_amount = st.number_input(
    "Loan Amount (₹)",
    min_value=0
)

if st.button("Predict Risk"):

    score = 0

    # Credit Score Analysis
    if credit_score >= 750:
        score += 3
    elif credit_score >= 600:
        score += 2
    else:
        score += 1

    # Income Analysis
    if income >= 50000:
        score += 3
    elif income >= 30000:
        score += 2
    else:
        score += 1

    # Loan Amount Analysis
    if loan_amount <= 300000:
        score += 3
    elif loan_amount <= 600000:
        score += 2
    else:
        score += 1

    # Final Risk Prediction
    if score >= 8:
        risk = "🟢 Low Risk"
    elif score >= 5:
        risk = "🟡 Medium Risk"
    else:
        risk = "🔴 High Risk"

    st.success(f"Predicted Risk Level: {risk}")
