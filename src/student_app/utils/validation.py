def get_valid_marks():
    while True:
        try:
            marks = int(input("\nEnter new marks: "))

            if marks < 0 or marks > 100:
                print("Invalid marks. Please enter a value between 0 and 100.")
                continue

            return marks

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_valid_semester():
    while True:
        try:
            semester = int(input("\nEnter new semester: "))

            if semester < 1 or semester > 8:
                print("Invalid semester. Please enter a value between 1 and 8.")
                continue

            return semester

        except ValueError:
            print("Invalid input. Please enter a number.")