from rapidfuzz import fuzz


def match_skills(text, skill_db):

    found_skills = []

    for category in skill_db:

        for skill, synonyms in skill_db[category].items():

            if skill in text:

                found_skills.append((skill, category, "direct"))

            for syn in synonyms:

                if syn in text:
                    found_skills.append((skill, category, "synonym"))

    return found_skills