def relevance_score(candidate_roles, job_role):

    score = 0

    for role in candidate_roles:

        if job_role.lower() in role.lower():
            score += 1

    if len(candidate_roles) == 0:
        return 0

    return round(score / len(candidate_roles), 2)