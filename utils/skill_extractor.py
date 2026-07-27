def extract_skills(text):

    skills_database = [
        "python",
        "java",
        "sql",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "data analysis",
        "pandas",
        "numpy",
        "scikit-learn",
        "tensorflow",
        "keras",
        "opencv",
        "flask",
        "django",
        "git",
        "github",
        "docker",
        "aws",
        "azure",
        "power bi",
        "tableau",
        "excel",
        "statistics",
        "communication",
        "leadership",
        "teamwork",
        "problem solving",
        "QuickBooks",
        "Diagram drawing",
        "Cooking and Baking"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills_database:
        if skill in text:
            found_skills.append(skill)

    return sorted(set(found_skills))