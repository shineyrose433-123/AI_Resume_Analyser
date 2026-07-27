import re


def extract_candidate_name(resume_text):
    """
    Attempts to extract the candidate's name from the resume.
    Falls back to 'Unknown Candidate' if no name is detected.
    """

    lines = [
        line.strip()
        for line in resume_text.split("\n")
        if line.strip()
    ]

    for line in lines[:10]:

        if len(line.split()) in [2, 3]:

            if re.fullmatch(r"[A-Za-z .'-]+", line):

                ignore_words = [
                    "resume",
                    "curriculum vitae",
                    "email",
                    "phone",
                    "address",
                    "linkedin",
                    "github",
                    "objective",
                    "summary",
                    "profile"
                ]

                if line.lower() not in ignore_words:
                    return line.title()

    return "Unknown Candidate"