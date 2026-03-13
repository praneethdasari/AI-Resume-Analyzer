import streamlit as st
from resume_reader import read_resume
from analyzer import analyze_resume

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])

if uploaded_file is not None:

    # Save uploaded resume
    with open("resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Extract resume text
    resume_text = read_resume("resume.pdf")

    st.write("Analyzing resume...")

    # Get AI analysis
    result = analyze_resume(resume_text)

    st.subheader("Analysis Result")
    st.write(result)