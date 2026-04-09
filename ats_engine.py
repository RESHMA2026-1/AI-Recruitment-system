def calculate_score(skill, experience, education, semantic, weights):
    final_score = (
        skill * weights["skill"] +
        experience * weights["experience"] +
        education * weights["education"] +
        semantic * weights["semantic"]
    )
    return final_score