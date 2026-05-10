import streamlit as st
import requests

st.title("Resume Screening App")

uploaded_file = st.file_uploader("Upload a resume (PDF)", type="pdf")

if uploaded_file is not None:
    st.write("File uploaded successfully", uploaded_file.name)
    print("File uploaded successfully", uploaded_file.name)

    if st.button("Process Resume"):
        response = requests.post(
            "http://localhost:8000/screening/",
            files={"resume": uploaded_file}
        )

        if response.status_code == 200:
            st.write("Resume processed successfully")
            response_data = response.json()
            st.write("Candidate details: ", response_data)
        else:
            st.write("Error processing resume")