def calculate_ats_score(match_score, matched_skills, total_skills):

    score = 0

    # Semantic Match (70%)
    score += match_score * 0.70

    # Skill Match (30%)
    if total_skills > 0:
        skill_percentage = (len(matched_skills) / total_skills) * 100
    else:
        skill_percentage = 0

    score += skill_percentage * 0.30

    return round(score, 2)