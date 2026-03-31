def detect_gaps(experience_list):

    gaps = []

    for i in range(len(experience_list) - 1):

        end = experience_list[i]["end"]
        start = experience_list[i+1]["start"]

        if end != start:
            gaps.append((end, start))

    return gaps