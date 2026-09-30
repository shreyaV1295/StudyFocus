def load_sessions():
    sessions = []

    try:
        file = open("study_sessions.txt", "r")

        for line in file:
            data = line.strip().split("|")

            if len(data) >= 8:
                distractions = { "Phone": int(data[3]),
                    "Social Media": int(data[4]),
                    "Talking": int(data[5]),
                    "Break": int(data[6]),
                    "Other": int(data[7]) }

                sessions.append({
                    "subject": data[0],
                    "study": int(data[1]),
                    "focus": int(data[2]),
                    "distractions": distractions})

        file.close()

    except FileNotFoundError:
        file = open("study_sessions.txt", "w")
        file.close()

    return sessions


def save_sessions(sessions):
    file = open("study_sessions.txt", "w")

    for s in sessions:
        d = s["distractions"]

        file.write( s["subject"] + "|" +
            str(s["study"]) + "|" +
            str(s["focus"]) + "|" +
            str(d["Phone"]) + "|" +
            str(d["Social Media"]) + "|" +
            str(d["Talking"]) + "|" +
            str(d["Break"]) + "|" +
            str(d["Other"]) + "\n")

    file.close()