from score_generator import generate_score

candidate = {
    "skill": 0.8,
    "experience": 0.7,
    "education": 0.9,
    "semantic": 0.75
}

result = generate_score(candidate)

print("Final Score:", result["final_score"])
print("Breakdown:", result["breakdown"])