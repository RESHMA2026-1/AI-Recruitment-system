from skill_extraction_engine.preprocess import clean_text
from skill_extraction_engine.skill_dictionary_loader import load_skill_dictionary, load_skill_stacks
from skill_extraction_engine.skill_matcher import match_skills
from skill_extraction_engine.confidence_score import get_confidence

skill_db = load_skill_dictionary()
stack_db = load_skill_stacks()


def extract_skills(text):

    text = clean_text(text)

    matches = match_skills(text, skill_db)

    results = []

    for skill, category, method in matches:

        confidence = get_confidence(method)

        results.append({
            "skill": skill,
            "type": category,
            "confidence": confidence
        })

    return results