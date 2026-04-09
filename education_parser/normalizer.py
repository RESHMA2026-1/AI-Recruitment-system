def normalize_degree(degree):
    mapping = {
        "B.Tech": "Bachelor of Technology",
        "MBA": "Master of Business Administration",
        "M.Tech": "Master of Technology"
    }

    for key in mapping:
        if key in degree:
            return mapping[key]

    return degree