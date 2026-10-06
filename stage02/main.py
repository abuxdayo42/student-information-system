def main():
    name = input("Enter student name: ")

    # Validate name
    if name == "":
        print("Invalid name")
        return

    marks = int(input("Enter marks: "))

    # Validate marks
    if marks < 0 or marks > 100:
        print("Invalid marks")
        return

    # Calculate grade
    if marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    print("\nStudent Report")
    print("----------------")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
