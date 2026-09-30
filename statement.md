# StudyFocus — Project Statement

# Project Title

**StudyFocus — Study Session and Distraction Analyzer**

=========================

# Problem Statement

Students often spend a significant amount of time studying but may not know how much of that time is actually focused.

Distractions such as mobile phones, social media, talking, unnecessary breaks, and other activities can reduce study productivity. Without tracking this information, it can be difficult for students to identify their common distractions and understand their study habits.

Therefore, there is a need for a simple system that allows students to record their study sessions, track distractions, and analyze their productivity.

=========================

# Proposed Solution

**StudyFocus** is a Python-based study tracking and distraction analysis system.

The program allows users to:

* Record the subject they studied.
* Enter total study time.
* Enter focused study time.
* Record different types of distractions.
* Calculate productivity percentage.
* Identify the main distraction.
* View individual study sessions.
* View an overall productivity report.
* Delete individual sessions.
* Delete all recorded sessions.
* Save study data for future use.

The system uses a text file to store the recorded sessions so that data remains available after the program is closed.

=========================

# Objectives

The main objectives of StudyFocus are:

1. To record and organize study sessions.
2. To measure focused study time.
3. To calculate study productivity.
4. To identify common sources of distraction.
5. To provide an overall study report.
6. To store data permanently using file handling.
7. To demonstrate modular programming in Python.
8. To create a simple and beginner-friendly productivity application.

=========================

# Scope of the Project

StudyFocus is designed primarily for students who want to understand and track their study habits.

The current version focuses on:

* Study session recording
* Focus time tracking
* Distraction tracking
* Productivity calculation
* Basic report generation
* Data storage

The project can later be expanded into a graphical or web-based application.

=========================

# Input

The program takes the following inputs from the user:

# Study Information

* Subject name
* Total study time
* Focused study time

# Distraction Information

* Phone
* Social Media
* Talking
* Break
* Other

The program validates the study and focus time before storing the session.

=========================

# Processing

The program performs the following operations:

# Productivity Calculation

The productivity percentage is calculated using:

Productivity = (Focused Time / Study Time) × 100

# Main Distraction

The program compares the number of distractions in each category and identifies the category with the highest count.

# Overall Analysis

For multiple sessions, the program calculates:

* Total study time
* Total focused time
* Overall productivity
* Most common distraction
* Focus level

=========================

# Output

The program displays:

* Individual study session details
* Study time
* Focused time
* Productivity percentage
* Main distraction
* Distraction counts
* Total number of sessions
* Overall study time
* Overall focused time
* Overall productivity
* Overall main distraction
* Focus level

=========================

# Focus Level

The program classifies productivity into three levels:

| Productivity | Focus Level |
| ------------ | ----------- |
| 75% or above | Good        |
| 50% – 74.99% | Moderate    |
| Below 50%    | Low         |

These categories are used only to summarize the calculated productivity percentage.

=========================

# Technologies Used

The project is developed using:

* **Python 3**
* Functions
* Modules
* Lists
* Dictionaries
* Loops
* Conditional statements
* Exception handling
* File handling
* Basic calculations

No external libraries are required.

=========================

# Modules Used

The project is divided into multiple Python files for modular programming.

StudyFocus
│
|_ main.py
|_ session.py
|_ storage.py
|_ analysis.py
|_ study_sessions.txt
|_ README.md
|_ statement.md

# main.py

Controls the main program and menu.

# session.py

Handles adding and deleting study sessions.

# storage.py

Handles reading and writing session data to the text file.

# analysis.py

Calculates productivity and generates study reports.

=========================

# Data Storage

The project uses a text file named:


study_sessions.txt


The data is stored using the `|` symbol as a separator.

Example:

Python|60|45|2|1|0|1|0

The stored information represents:

Subject | Study Time | Focus Time | Phone | Social Media | Talking | Break | Other

This allows previously recorded sessions to be loaded when the program starts.

=========================

# Advantages

* Simple and easy to use.
* Beginner-friendly.
* Does not require external libraries.
* Stores data permanently.
* Helps users understand their study patterns.
* Identifies common distractions.
* Uses modular Python programming.
* Can be easily extended with additional features.

=========================

# Limitations

The current version has some limitations:

* It uses a command-line interface.
* Data is stored in a simple text file.
* It does not have user accounts.
* It does not provide graphical charts.
* It does not automatically track study time.
* It does not provide online synchronization.

=========================

# Future Enhancements

Possible future improvements include:

1. Adding graphs and charts.
2. Adding date and time for every session.
3. Adding weekly and monthly reports.
4. Creating a graphical user interface.
5. Adding study reminders.
6. Adding automatic timers.
7. Adding user accounts.
8. Exporting reports to CSV or PDF.
9. Creating a web-based version.
10. Adding a database such as SQLite.

=========================

# Expected Outcome

The expected outcome of this project is a functional Python application that allows students to record their study sessions and distractions and provides a simple analysis of their productivity.

The project also demonstrates practical application of fundamental Python programming concepts such as functions, modules, data structures, file handling, loops, conditional statements, and exception handling.

=========================

# Conclusion

StudyFocus provides a simple approach to recording study sessions and analyzing distractions. By tracking focused time and distraction patterns, users can obtain a clearer picture of their study sessions.

The project demonstrates how basic Python programming concepts can be combined to create a useful real-world application. Its modular structure also makes the program easier to understand, maintain, and expand in the future.

=========================