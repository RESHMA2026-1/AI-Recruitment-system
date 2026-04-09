from models import Education, Certification

def extract_education(text):
    education_list = []
    lines = text.split("\n")

    for line in lines:
        if any(deg in line for deg in ["B.Tech", "MBA", "M.Tech", "BSc", "MSc"]):
            parts = line.split(",")

            if len(parts) >= 3:
                degree = parts[0]
                institution = parts[1].strip()
                year = parts[2].strip()

                education_list.append(
                    Education(degree, "Unknown", institution, year)
                )

    return education_list


def extract_certifications(text):
    certs = []

    lines = text.split("\n")

    for line in lines:
        if "certified" in line.lower():
            certs.append(Certification(line.strip()))

    return certs