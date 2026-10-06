def main():
    name = input("Enter student name: ")

    # Validation
    if name == "":
        print("Invalid name")
        return

    # Calculation
    marks = 80
    bonus = 5
    total_marks = marks + bonus

    print(f"Student: {name}")
    print(f"Total Marks: {total_marks}")


if __name__ == "__main__":
    main()
