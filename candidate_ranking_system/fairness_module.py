# fairness_module.py

def normalize_resume(resume):
    return {
        "name": resume.get("name", "").lower(),
        "skills": [s.lower() for s in resume.get("skills", [])],
        "experience": float(resume.get("experience", 0)),
        "education": resume.get("education", "").lower()
    }

def mask_sensitive_info(resume):
    resume["name"] = "MASKED"
    return resume

def skill_match_score(job_skills, resume_skills):
    match = set(job_skills).intersection(set(resume_skills))
    return len(match) / len(job_skills)

def run_fairness_module(resume, job_skills):
    resume = normalize_resume(resume)
    resume = mask_sensitive_info(resume)
    score = skill_match_score(job_skills, resume["skills"])
    return score
def normalize_score(score, min_score, max_score):
    if max_score == min_score:
        return 1
    return (score - min_score) / (max_score - min_score)