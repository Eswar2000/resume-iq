import streamlit as st
import requests

st.title("Resume Screening App")

uploaded_file = st.file_uploader("Upload a resume (PDF)", type="pdf")

if uploaded_file is not None:
    st.toast(f"File \"{uploaded_file.name}\" uploaded successfully", icon="🎉", duration="short")

    if st.button("Process Resume"):
        with st.spinner("Procesing resume..."):
            response = requests.post(
                "http://localhost:8000/screening/",
                files={"resume": uploaded_file}
            )

            if response.status_code == 200:
                st.toast("Resume processed successfully", icon="✅", duration="short")
                response_data = response.json()
                st.write("Candidate details: ", response_data)
            else:
                st.toast("Error processing resume", icon="🚨", duration="short")