import pandas as pd
import streamlit as st
from utils.candidate_name import extract_candidate_name
from utils.ats_score import calculate_ats_score
from utils.resume_parser import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from models.matcher import calculate_match_score


st.set_page_config(
    page_title="ResumeAI Pro",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 ResumeAI Pro")
st.subheader("AI-Powered Recruitment Assistant")

st.write(
    """
    Upload multiple resumes, compare them against a job description,
    and rank candidates using AI-powered semantic matching.
    """
)


st.divider()

st.header("💼 Job Description")

job_description = st.text_area(
    "Paste the Job Description",
    height=220,
    placeholder="Example: Looking for a Machine Learning Engineer with Python, SQL, Machine Learning, TensorFlow..."
)


st.divider()

st.header("📂 Upload Candidate Resumes")

uploaded_resumes = st.file_uploader(
    "Upload one or more PDF resumes",
    type=["pdf"],
    accept_multiple_files=True
)


st.divider()


if st.button("🚀 Analyze Candidates"):

    if not job_description.strip():
        st.warning("Please paste a Job Description.")
        st.stop()

    if not uploaded_resumes:
        st.warning("Please upload at least one resume.")
        st.stop()


    clean_jd = clean_text(job_description)
    jd_skills = extract_skills(clean_jd)

    results = []

    st.success(
        f"Successfully uploaded {len(uploaded_resumes)} resume(s)."
    )


    for index, resume in enumerate(uploaded_resumes, start=1):

        resume_text = extract_text_from_pdf(resume)
        candidate_name = extract_candidate_name(resume_text)

        if not resume_text.strip():
            st.warning(
                f"Could not extract text from {resume.name}"
            )
            continue


        clean_resume = clean_text(resume_text)


        match_score = calculate_match_score(
            clean_resume,
            clean_jd
        )


        resume_skills = extract_skills(clean_resume)


        matched_skills = sorted(
            list(set(resume_skills) & set(jd_skills))
        )


        missing_skills = sorted(
            list(set(jd_skills) - set(resume_skills))
        )


        ats_score = calculate_ats_score(
            match_score,
            matched_skills,
            len(jd_skills)
        )


        missing_skill_count = len(missing_skills)

        if match_score >= 80 and missing_skill_count <= 2:
          decision = "🟢 Shortlisted"

        elif match_score >= 60 and missing_skill_count <= 4:
          decision = "🟡 Review"

        else:
          decision = "🔴 Rejected"


        results.append({
          "Candidate": candidate_name,
          "Resume File": resume.name,
          "AI Match (%)": round(match_score, 2),
          "ATS Score (%)": round(ats_score, 2),
          "Matched Skills": len(matched_skills),
          "Missing Skills": len(missing_skills),
          "Decision": decision
        })


        st.divider()

        st.subheader(f"👤 {candidate_name}")
        st.caption(f"Resume: {resume.name}")


        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("🎯 AI Match", f"{match_score:.2f}%")

        with col2:
            st.metric("📊 ATS Score", f"{ats_score:.2f}%")

        with col3:
            st.metric("📄 Resume Size", f"{round(resume.size / 1024, 2)} KB")

        with col4:
            if decision == "🟢 Shortlisted":
                st.metric("📌 Decision", "Shortlisted")

            elif decision == "🟡 Review":
                st.metric("📌 Decision", "Review")

            else:
                st.metric("📌 Decision", "Rejected")


        st.markdown("### ✅ Matched Skills")

        if matched_skills:
            st.success(", ".join(matched_skills))
        else:
            st.warning("No matching skills found.")


        st.markdown("### ❌ Missing Skills")


        if missing_skills:
            st.error(", ".join(missing_skills))
        else:
            st.success("No missing skills found.")


        with st.expander("📄 View Resume Text"):

            st.text_area(
                "Resume Content",
                resume_text,
                height=250,
                key=f"resume_{index}"
            )


    if results:

        st.divider()

    st.success("✅ Analysis completed successfully!")

    results_df = pd.DataFrame(results)

    results_df = results_df.sort_values(
        by="ATS Score (%)",
        ascending=False
    ).reset_index(drop=True)

    results_df.index = results_df.index + 1

    total_candidates = len(results_df)

    shortlisted = len(
        results_df[results_df["Decision"] == "🟢 Shortlisted"]
    )

    review = len(
        results_df[results_df["Decision"] == "🟡 Review"]
    )

    rejected = len(
        results_df[results_df["Decision"] == "🔴 Rejected"]
    )

    average_ats = round(results_df["ATS Score (%)"].mean(), 2)

    highest_ats = round(results_df["ATS Score (%)"].max(), 2)

    lowest_ats = round(results_df["ATS Score (%)"].min(), 2)

    st.header("📊 Recruitment Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📄 Total Resumes", total_candidates)

    with col2:
        st.metric("🟢 Shortlisted", shortlisted)

    with col3:
        st.metric("🟡 Review", review)

    with col4:
        st.metric("🔴 Rejected", rejected)

    st.divider()

    st.subheader("📈 Recruitment Insights")

    st.info(
        f"""
📄 Total resumes analyzed : {total_candidates}

📊 Average ATS Score : {average_ats}%

🏆 Highest ATS Score : {highest_ats}%

📉 Lowest ATS Score : {lowest_ats}%

⭐ Recommended Candidates : {shortlisted}
"""
    )

    st.divider()

    st.header("🏆 Candidate Ranking")

    st.dataframe(
        results_df,
        use_container_width=True
    )

    csv = results_df.to_csv(index=False)

    st.download_button(
        label="📥 Download Results as CSV",
        data=csv,
        file_name="candidate_rankings.csv",
        mime="text/csv"
    )

else:
    st.warning("No valid resumes could be analyzed.")
