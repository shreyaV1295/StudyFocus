from storage import save_sessions


def add_session(sessions):
    subject = input("Enter subject: ")

    try:
        study = int(input("Enter study time (minutes): "))
        focus = int(input("Enter focused time (minutes): "))

        if study <= 0 or focus < 0 or focus > study:
            print("Invalid time.")
            return

    except ValueError:
        print("Enter numbers only.")
        return

    print("\nDISTRACTED BY")

    types = ["Phone", "Social Media", "Talking", "Break", "Other"]
    distractions = {}

    for item in types:
        count = input(item + ": ")

        if count.isdigit():
            distractions[item] = int(count)
        else:
            distractions[item] = 0

    sessions.append({"subject": subject,
        "study": study,
        "focus": focus,
        "distractions": distractions})

    save_sessions(sessions)

    print("Session added successfully.")


def delete_session(sessions):
    if not sessions:
        print("No sessions to delete.")
        return

    print("\nDELETE SESSION")
    print("1. Delete Particular Session")
    print("2. Delete All Sessions")
    print("3. Cancel")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            number = int(input("Enter session number to delete: "))

            if 1 <= number <= len(sessions):
                sessions.pop(number - 1)
                save_sessions(sessions)
                print("Session", number, "deleted successfully.")
            else:
                print("Invalid session number.")

        except ValueError:
            print("Enter a valid number.")

    elif choice == "2":
        sessions.clear()
        save_sessions(sessions)
        print("All sessions deleted successfully.")

    elif choice == "3":
        print("Cancelled.")

    else:
        print("Invalid choice.")