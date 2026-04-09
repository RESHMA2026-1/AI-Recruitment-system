from ats_engine import calculate_score
from weights_config import weights

def generate_score(candidate):
    skill = candidate.get("skill", 0)
    experience = candidate.get("experience", 0)
    education = candidate.get("education", 0)
    semantic = candidate.get("semantic", 0)

    final_score = calculate_score(skill, experience, education, semantic, weights)

    return {
        "final_score": final_score,
        "breakdown": {
            "skill": skill,
            "experience": experience,
            "education": education,
            "semantic": semantic
        }
    }