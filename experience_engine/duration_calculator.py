from datetime import datetime

def calculate_duration(start, end):

    start_date = datetime.strptime(start, "%b %Y")

    if end.lower() == "present":
        end_date = datetime.now()
    else:
        end_date = datetime.strptime(end, "%b %Y")

    duration = end_date - start_date

    return round(duration.days / 365, 2)