# frontend_streamlit/app.py

import streamlit as st
import requests

API_URL = "http://backend:8000"


st.title("📘 JLPT Story Generator")

# JLPT Level Selection
level = st.selectbox(
    "Select JLPT Level",
    ["N5", "N4", "N3", "N2", "N1"]
)

# Generate Button
if st.button("Generate Story"):
    with st.spinner("Generating story..."):
        response = requests.post(
            f"{API_URL}/generate-story",
            json={"level": level}
        )

        if response.status_code == 200:
            data = response.json()
            st.subheader("Story")
            st.write(data["story"])
        else:
            st.error("Failed to generate story")