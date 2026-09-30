# StudyFocus

**StudyFocus** is a beginner-friendly Python project that helps students record study sessions, track distractions, and analyze their study productivity.

=====================


# Project Objective

The project helps users understand their study habits by recording:

* Subject studied
* Total study time
* Focused study time
* Phone distractions
* Social Media distractions
* Talking
* Breaks
* Other distractions

=====================


# Features

* Add study sessions
* Calculate productivity percentage
* Identify the main distraction
* View individual and overall reports
* Delete a particular session
* Delete all sessions
* Save data using a text file
* Load previous sessions when the program starts

=====================


# Technologies Used

* Python 3
* Functions
* Lists and Dictionaries
* Loops and Conditions
* Exception Handling
* File Handling
* Python Modules

No external libraries are required.

=====================


# Project Structure

StudyFocus
│
|_ main.py
|_ session.py
|_ storage.py
|_ analysis.py
|_ study_sessions.txt
|_ README.md
|_ statement.md

=====================


# Files

**main.py** — Controls the main menu and program flow.

**session.py** — Adds and deletes study sessions.

**storage.py** — Saves and loads session data.

**analysis.py** — Calculates productivity and generates reports.

**study_sessions.txt** — Stores saved study-session data.

=====================


# Productivity Formula

Productivity = (Focused Time / Study Time) × 100

=====================


# Focus Levels

| Productivity | Level    |
| ------------ | -------- |
| 75% or above | Good     |
| 50% – 74.99% | Moderate |
| Below 50%    | Low      |

=====================


# How to Run

1. Install **Python 3**.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run: python main.py

=====================


# Example

       STUDYFOCUS

1. Add Study Session
2. View Sessions & Report
3. Delete Session
4. Exit

Enter your choice:

## Example input
Enter subject : Python
Enter study time(minutes): 60
Enter focused time(minutes): 45

Distracted by

Phone: 2
Social Media: 1
Talking: 0
Break: 1
Other: 0

## Example Report
STUDY SESSIONS

SESSION 1
Subject: Python
Study Time: 60 minutes
Focused Time: 45 minutes
Productivity: 75.0 %
Main Distraction: Phone

Distractions:
Phone: 2
Social Media: 1
Break: 1

OVERALL REPORT
Sessions: 1
Study Time: 60 minutes
Focused Time: 45 minutes
Productivity: 75.0 %
Main Distraction: Phone
Focus Level: Good

=====================