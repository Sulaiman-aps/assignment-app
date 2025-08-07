streamlit
pandas
import streamlit as st
import pandas as pd

st.title("📚 Assignment Request Form")

name = st.text_input("Full Name")
city = st.text_input("City")
phone = st.text_input("Phone Number")
payment = st.selectbox("Payment Method", ["Bank Transfer", "PayPal", "Credit Card", "Other"])

if st.button("Submit Request"):
    new_data = pd.DataFrame({
        "Name": [name],
        "City": [city],
        "Phone": [phone],
        "Payment": [payment]
    })

    try:
        existing = pd.read_csv("requests.csv")
        updated = pd.concat([existing, new_data], ignore_index=True)
    except FileNotFoundError:
        updated = new_data

    updated.to_csv("requests.csv", index=False)
    st.success("✅ Assignment request submitted successfully!")

