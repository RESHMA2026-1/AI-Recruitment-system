from .embedding_engine import get_embedding
from .similarity_engine import calculate_similarity

def match_resume_to_jd(resume_text, jd_text):

    resume_vec = get_embedding(resume_text)
    jd_vec = get_embedding(jd_text)

    score = calculate_similarity(resume_vec, jd_vec)

    return score