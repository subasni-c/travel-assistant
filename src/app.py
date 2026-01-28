import streamlit as st
import requests
FASTAPI_URL = "http://localhost:8000"

st.title("🧭 AI Travel Itinerary Assistant")
st.markdown("Ask about any travel destination - we'll find the best suggestions for you!")

# Sidebar for File Upload
with st.sidebar:
    st.subheader("📁 Upload Travel Guide")
    uploaded_file = st.file_uploader("Upload a PDF travel guide (optional)", type="pdf")

    if uploaded_file:
        if st.button("Process Guide"):
            with st.spinner("Processing the travel guide..."):
                st.success("file uploaded sucessfully")

# Main content
st.subheader("❓ Ask Your Question")
query = st.text_input("Enter your travel question (e.g., Best places to visit in Paris):")

if st.button("Ask"):
    if query.strip():
        with st.spinner("Thinking..."):
            st.success("hello my friend!!")
    else:
        st.warning("Please enter a query.")
