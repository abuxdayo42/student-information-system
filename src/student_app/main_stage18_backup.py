import json

from src.student_app.config import APP_NAME, DEBUG, MAX_STUDENTS, API_KEY


def main():
    print(f"Application Name: {APP_NAME}")
    print(f"Debug Mode: {DEBUG}")
    print(f"Maximum Students: {MAX_STUDENTS}")

    if API_KEY:
        print("API Key loaded successfully.")
    else:
        print("API Key was not loaded.")

    with open("data/student.json", "r") as file:
        student = json.load(file)

    print("\nStudent Information")
    print("-------------------")
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Program: {student['program']}")
    print(f"Semester: {student['semester']}")
    print(f"Marks: {student['marks']}")


if __name__ == "__main__":
    main()