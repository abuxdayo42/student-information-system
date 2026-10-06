from validation import validate_name, validate_marks
from calculator import calculate_grade


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

    print("\nStudent Report")
    print("----------------")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
