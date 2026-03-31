import re

def parse_experience(text):

    pattern = r'([A-Za-z ]+) – ([A-Za-z ]+)\n([A-Za-z0-9 ]+) – ([A-Za-z0-9 ]+)'

    matches = re.findall(pattern, text)

    results = []

    for role, company, start, end in matches:

        results.append({
            "company": company.strip(),
            "role": role.strip(),
            "start": start.strip(),
            "end": end.strip()
        })

    return results