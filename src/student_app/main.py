from src.student_app.config import APP_NAME, DEBUG, MAX_STUDENTS, API_KEY
from src.student_app.services.student_service import load_student, save_student
from src.student_app.utils.validation import get_valid_marks, get_valid_semester
from src.student_app.utils.logger import logger


def display_config():
    print(f"Application Name: {APP_NAME}")
    print(f"Debug Mode: {DEBUG}")
    print(f"Maximum Students: {MAX_STUDENTS}")

    if API_KEY:
        print("API Key loaded successfully.")
    else:
        print("API Key not found.")


def display_student(student):
    print("\nStudent Information")
    print("-------------------")
    print(f"ID: {student.student_id}")
    print(f"Name: {student.name}")
    print(f"Program: {student.program}")
    print(f"Semester: {student.semester}")
    print(f"Marks: {student.marks}")

    logger.info("Student information displayed.")


def update_marks(student):
    original_marks = student.marks

    new_marks = get_valid_marks()

    student.update_marks(new_marks)

    if save_student(student):
        print("\nMarks updated successfully.")
        print("Student data saved successfully.")
        print(f"Original Marks: {original_marks}")
        print(f"New Marks: {student.marks}")

        logger.info(
            f"Student marks updated from {original_marks} to {new_marks}."
        )

    else:
        student.update_marks(original_marks)

        print("\nMarks update failed.")
        print("Original marks have been restored.")

        logger.error("Failed to save updated student marks.")


def update_semester(student):
    original_semester = student.semester

    new_semester = get_valid_semester()

    student.update_semester(new_semester)

    if save_student(student):
        print("\nSemester updated successfully.")
        print("Student data saved successfully.")
        print(f"Original Semester: {original_semester}")
        print(f"New Semester: {student.semester}")

        logger.info(
            f"Student semester updated from {original_semester} to {new_semester}."
        )

    else:
        student.update_semester(original_semester)

        print("\nSemester update failed.")
        print("Original semester has been restored.")

        logger.error("Failed to save updated student semester.")


def show_menu():
    print("\nStudent Management System")
    print("-------------------------")
    print("1. View Student")
    print("2. Update Marks")
    print("3. Update Semester")
    print("4. Exit")


def main():
    logger.info("Application started.")

    display_config()

    student = load_student()

    if student is None:
        print("\nUnable to load student data.")
        print("Exiting application...")

        logger.error("Application stopped because student data could not be loaded.")
        return

    logger.info("Student data loaded successfully.")

    while True:
        show_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_student(student)

        elif choice == "2":
            update_marks(student)

        elif choice == "3":
            update_semester(student)

        elif choice == "4":
            print("\nExiting application...")
            logger.info("Application exited normally.")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, 3, or 4.")
            logger.warning(f"Invalid menu choice entered: {choice}")


if __name__ == "__main__":
    main()