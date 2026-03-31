print("AI Recruitment System Started")

required_skills = ["python", "machine learning", "communication"]

resume = input("Enter candidate skills separated by comma: ")

candidate_skills = resume.lower().split(",")

candidate_skills = [skill.strip() for skill in candidate_skills]

match_count = 0

for skill in required_skills:
    if skill in candidate_skills:
        match_count += 1 

score = (match_count / len(required_skills)) * 100

print("Match Score:", score, "%")

if score >= 70:
    print("Candidate Selected ✅")
else:
    print("Candidate Rejected ❌")

