# candidate_ranking.py

from fairness_module import run_fairness_module

# Job required skills
job_skills = ["python", "sql", "ml"]

# Candidate data (no score here ❌)
candidates = [
    {"name": "Anu", "skills": ["python", "sql"]},
    {"name": "Rahul", "skills": ["java", "ml"]},
    {"name": "Meena", "skills": ["html", "css"]}
]

# 🔥 Generate score using fairness module
for c in candidates:
    c["score"] = run_fairness_module(c, job_skills)

# Step 1: Rank candidates
candidates = sorted(candidates, key=lambda x: x["score"], reverse=True)

# Step 2: Apply shortlisting rules
for c in candidates:
    if c["score"] >= 0.8:
        c["status"] = "Shortlisted"
    elif c["score"] >= 0.5:
        c["status"] = "Review"
    else:
        c["status"] = "Rejected"
        # Normalize scores
scores = [c["score"] for c in candidates]

min_score = min(scores)
max_score = max(scores)

from fairness_module import normalize_score

for c in candidates:
    c["score"] = normalize_score(c["score"], min_score, max_score)

# Final Output
for c in candidates:
    print("Name:", c["name"])
    print("Score:", round(c["score"], 2))
    print("Status:", c["status"])
    print("----------------------")