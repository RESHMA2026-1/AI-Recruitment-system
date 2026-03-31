def get_confidence(method):

    scores = {
        "direct": 0.95,
        "synonym": 0.90,
        "stack": 0.85,
        "nlp": 0.80,
        "fuzzy": 0.70
    }

    return scores.get(method, 0.60)