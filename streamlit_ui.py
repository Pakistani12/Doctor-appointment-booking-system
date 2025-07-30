import streamlit as st
import requests

st.title("🏥 Medical Chatbot & Appointment System")
name = st.text_input("Enter your name")
phone = st.text_input("Enter your phone number")
query = st.text_area("Ask a medical question or book an appointment")

if st.button("Submit"):
    if name and phone and query:
        response = requests.post("http://localhost:8000/chat", json={"name": name, "phone": phone, "query": query})
        st.success(response.json().get("reply"))
    else:
        st.warning("Please fill all fields")