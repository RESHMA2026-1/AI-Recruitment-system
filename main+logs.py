from logs import log_info, log_error

print("AI Recruitment System Started")

log_info("Program started")

try:
    required_skills = ["python", "machine learning", "communication"]

    resume = input("Enter candidate skills separated by comma: ")
    log_info(f"User entered skills: {resume}")

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
        log_info("Candidate Selected")
    else:
        print("Candidate Rejected ❌")
        log_info("Candidate Rejected")

except Exception as e:
    print("An error occurred:", e)
    log_error(str(e))

