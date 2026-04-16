import streamlit as st
from utils import extract_text_from_pdf, analyze_resume
from skills import SKILLS
from sample_jobs import JOB_ROLES

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and check how well it matches a job role!")

# Upload PDF
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Select job role
job_role = st.selectbox("Select Job Role", list(JOB_ROLES.keys()))

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)

    st.subheader("📃 Extracted Resume Text")
    st.text_area("", text, height=200)

    result = analyze_resume(text, job_role)

    st.subheader("📊 Analysis Results")

    st.write(f"✅ **Resume Score:** {result['score']}%")

    st.write("🧠 **Matched Skills:**")
    st.write(result["matched_skills"])

    st.write("❌ **Missing Skills:**")
    st.write(result["missing_skills"])

    st.subheader("💡 Suggestions to Improve")

    for suggestion in result["suggestions"]:
        st.write(f"- {suggestion}")