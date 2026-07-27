# 🤖 AI Resume Analyser

An AI-powered Resume Screening and ATS Analysis system developed using Python and Streamlit that helps recruiters efficiently evaluate, rank, and shortlist candidates based on a given Job Description.


##  Features

- Upload multiple PDF resumes simultaneously
- Paste any Job Description
- AI-based Resume Matching
- ATS Score Calculation
- Skill Extraction
- Matched Skills Detection
- Missing Skills Detection
- Automatic Candidate Ranking
- Shortlist / Review / Reject Recommendation
- Resume Text Viewer
- Recruitment Dashboard
- CSV Report Export


##  Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- Sentence Transformers
- NLP
- PDFPlumber
- Git
- GitHub


## Project Structure

```
AI_Resume_Analyser
│
├── app.py
├── requirements.txt
├── README.md
│
├── models
│     └── matcher.py
│
├── utils
│     ├── ats_score.py
│     ├── candidate_name.py
│     ├── resume_parser.py
│     ├── skill_extractor.py
│     └── text_cleaner.py
│
├── assets
├── uploads
└── data
```

---

## 📊 Workflow

1. Recruiter pastes the Job Description.
2. Uploads multiple candidate resumes.
3. The application extracts resume text.
4. Skills are identified using NLP.
5. AI Match Score is calculated.
6. ATS Score is generated.
7. Missing skills are identified.
8. Candidates are ranked automatically.
9. Final report can be downloaded as CSV.


## Output

The application provides:

- AI Match Score
- ATS Score
- Matched Skills
- Missing Skills
- Candidate Recommendation
- Candidate Ranking
- CSV Export


##  Future Improvements

- Resume Parsing using LLMs
- Semantic Skill Matching
- Recruiter Login Dashboard
- Cloud Deployment
- Interview Recommendation Engine
- Candidate Analytics Dashboard


##  Author

Shiney Rose.S

B.Tech Artificial Intelligence & Data Science

Python | Machine Learning | Data Science | AI
