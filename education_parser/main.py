from extractor import extract_education, extract_certifications
from normalizer import normalize_degree
from relevance import tag_certification

def run_pipeline(text):

    education = extract_education(text)
    certifications = extract_certifications(text)

    # Normalize
    for edu in education:
        edu.degree = normalize_degree(edu.degree)

    # Tag certifications
    for cert in certifications:
        cert.category = tag_certification(cert)

    return education, certifications


if __name__ == "__main__":
    with open("test_data/sample_resume.txt", "r") as f:
        text = f.read()

    education, certifications = run_pipeline(text)

    print("\nEDUCATION:")
    for edu in education:
        print(vars(edu))

    print("\nCERTIFICATIONS:")
    for cert in certifications:
        print(vars(cert))