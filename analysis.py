def view_report(sessions):

    if not sessions:
        print("No sessions recorded.")
        return

    total_study = 0
    total_focus = 0
    all_distractions = {}

    print("\nSTUDY SESSIONS")

    for i in range(len(sessions)):

        s = sessions[i]

        total_study += s["study"]
        total_focus += s["focus"]

        for item, count in s["distractions"].items():
            all_distractions[item] = (all_distractions.get(item, 0) + count)

        productivity = (s["focus"] / s["study"]) * 100

        if sum(s["distractions"].values()) > 0:
            common = max(s["distractions"],
                key=s["distractions"].get)
        else:
            common = "None"

        print("\nSESSION", i + 1)
        print("Subject:", s["subject"])
        print("Study Time:", s["study"], "minutes")
        print("Focused Time:", s["focus"], "minutes")
        print("Productivity:", round(productivity, 2), "%")
        print("Main Distraction:", common)

        print("Distractions:")

        found = False

        for item, count in s["distractions"].items():
            if count > 0:
                print(item + ":", count)
                found = True

        if not found:
            print("None")

    productivity = (total_focus / total_study) * 100

    if sum(all_distractions.values()) > 0:
        common = max(all_distractions, key=all_distractions.get)
    else:
        common = "None"

    print("\nOVERALL REPORT")
    print("Sessions:", len(sessions))
    print("Study Time:", total_study, "minutes")
    print("Focused Time:", total_focus, "minutes")
    print("Productivity:", round(productivity, 2), "%")
    print("Main Distraction:", common)

    if productivity >= 75:
        print("Focus Level: Good")
    elif productivity >= 50:
        print("Focus Level: Moderate")
    else:
        print("Focus Level: Low")