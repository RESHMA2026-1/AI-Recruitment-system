from experience_engine.experience_parser import parse_experience
from experience_engine.relevance_engine import relevance_score

resume_text = """
Software Engineer – TCS
Jan 2021 – Mar 2023

Python Developer – Infosys
Apr 2023 – Present
"""

job_role = "Python Developer"

experience = parse_experience(resume_text)

roles = [job["role"] for job in experience]

score = relevance_score(roles, job_role)

structured_experience = {
    "candidate_id": "C101",
    "experience": experience,
    "experience_relevance_score": score
}

print("Structured Experience Object:")
print(structured_experience)