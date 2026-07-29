# 🤖 AI Resume Analyser

An AI-powered resume screening and candidate ranking application built with **Python** and **Streamlit**. The system analyzes multiple resumes against a given job description, calculates AI Match and ATS scores, identifies relevant skills, and automatically ranks candidates to assist recruiters in making faster and more informed hiring decisions.


##  Live Demo

🔗 https://ai-resume-analyser-rose.streamlit.app



## Features

- Upload and analyze multiple PDF resumes simultaneously
- Compare resumes against any job description
- AI-powered semantic resume matching
- ATS score calculation
- Automatic skill extraction
- Identification of matched and missing skills
- Intelligent candidate recommendation (Shortlisted / Review / Rejected)
- Candidate ranking based on ATS score
- Interactive recruitment dashboard
- Resume content viewer
- Export candidate rankings as a CSV report


##  Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Sentence Transformers
- PDFPlumber
- Natural Language Processing (NLP)
- Git & GitHub

---

##  Project Structure

```text
AI_Resume_Analyser
│
├── app.py
├── requirements.txt
├── README.md
│
├── models
│   └── matcher.py
│
├── utils
│   ├── ats_score.py
│   ├── candidate_name.py
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   └── text_cleaner.py
│
├── assets
  ├── screenshots

```


##  How It Works

1. Enter the job description.
2. Upload one or more PDF resumes.
3. Resume text is extracted automatically.
4. Relevant skills are identified from both the job description and resumes.
5. An AI Match Score is calculated using semantic similarity.
6. An ATS Score is generated based on AI similarity and skill matching.
7. Missing and matched skills are displayed for every candidate.
8. Candidates are categorized as **Shortlisted**, **Review**, or **Rejected**.
9. A ranked candidate list is generated and can be exported as a CSV report.


## Output

For every uploaded resume, the application provides:

- 👤 Candidate Name
- 📄 Resume File Name
- 🎯 AI Match Score
- 📊 ATS Score
- ✅ Matched Skills
- ❌ Missing Skills
- 📌 Hiring Recommendation
- 🏆 Candidate Ranking

The dashboard also displays:

- Total resumes analyzed
- Number of shortlisted candidates
- Candidates requiring review
- Rejected candidates
- Average ATS score
- Highest ATS score
- Lowest ATS score


##  Use Cases

This project can be used by:

- Recruiters
- HR professionals
- Hiring teams
- Placement cells
- Students learning AI and NLP
- Anyone interested in automated resume screening


##  Future Enhancements

- Advanced resume parsing using Large Language Models (LLMs)
- Semantic skill matching with skill synonyms
- Recruiter authentication and login system
- Cloud deployment
- Candidate interview recommendation engine
- Interactive analytics dashboard
- Resume scoring explanation and feedback generation


## Author

Shiney Rose S

B.Tech – Artificial Intelligence & Data Science

Passionate about Artificial Intelligence, Machine Learning, Data Science, and building practical AI applications that solve real-world problems.
