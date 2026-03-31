def tag_certification(cert):
    name = cert.name.lower()

    if "python" in name:
        return "Programming"

    elif "aws" in name:
        return "Cloud"

    elif "data" in name:
        return "Data Science"

    else:
        return "General"