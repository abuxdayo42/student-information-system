from validation import validate_name, validate_marks
from calculator import calculate_grade
from student import Student
from report import display_report


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

    display_report(student)


if __name__ == "__main__":
    main()
