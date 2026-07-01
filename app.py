import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="ResumeAI Pro",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("📄 ResumeAI Pro")
st.subheader("AI-Powered Resume Screening & ATS Analyzer")

st.markdown("---")

st.write("""
Welcome to **ResumeAI Pro** 🚀

This application will help you:

✅ Upload your resume

✅ Compare it with a Job Description

✅ Calculate AI Match Score

✅ Analyze ATS Compatibility

✅ Detect Missing Skills

✅ Suggest Resume Improvements

---
""")

st.info("Project Version: 0.1")