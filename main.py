from storage import load_sessions
from session import add_session, delete_session
from analysis import view_report


sessions = load_sessions()


while True:

    print("\n========================")
    print("       STUDYFOCUS")
    print("========================")
    print("1. Add Study Session")
    print("2. View Sessions & Report")
    print("3. Delete Session")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_session(sessions)

    elif choice == "2":
        view_report(sessions)

    elif choice == "3":
        delete_session(sessions)

    elif choice == "4":
        print("Thank you for using StudyFocus.")
        break

    else:
        print("Invalid choice. Please try again.")