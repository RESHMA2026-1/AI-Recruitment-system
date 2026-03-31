from skill_extraction_engine.skill_engine import extract_skills

resume_text = """
Experienced Python developer with Machine Learning knowledge.
Worked with React and NodeJS.
Strong leadership and communication skills.
"""

skills = extract_skills(resume_text)

print(skills)