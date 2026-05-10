import streamlit as st
import requests

if "processing" not in st.session_state:
    st.session_state.processing = False

st.title("Resume Screening App")

uploaded_file = st.file_uploader("Upload a resume (PDF)", type="pdf")

if uploaded_file is not None:
    st.toast(f"File \"{uploaded_file.name}\" uploaded successfully", icon="🎉", duration="short")

    process_resume_clicked = st.button(
        "Process Resume",
        disabled=st.session_state.processing
    )
    if process_resume_clicked:
        st.session_state.processing = True
        with st.status("Procesing resume...", expanded=True) as status:
            response = requests.post(
                "http://localhost:8000/screening/",
                files={"resume": uploaded_file}
            )

            if response.status_code == 200:
                response_data = response.json()
                status.update(label="Resume processed successfully!", state="complete")
                st.toast("Resume processed successfully", icon="✅", duration="short")
                
                st.subheader("Candidate Details")
                st.json(response_data)
            else:
                status.update(label="Error processing resume", state="error")
                st.toast("Error processing resume", icon="🚨", duration="short")