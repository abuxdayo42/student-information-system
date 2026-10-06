from utils.validation import validate_name, validate_marks
from services.calculator import calculate_grade
from models.student import Student


def main():
    name = input("Enter student name: ")

    if not validate_name(name):
        print("Invalid name")
        return

    marks = int(input("Enter marks: "))

    if not validate_marks(marks):
        print("Invalid marks")
        return

    grade = calculate_grade(marks)

    student = Student(name, marks, grade)

    details = student.get_details()

    print("\nStudent Report")
    print("----------------")
    print(f"Name: {details['name']}")
    print(f"Marks: {details['marks']}")
    print(f"Grade: {details['grade']}")


if __name__ == "__main__":
    main()
