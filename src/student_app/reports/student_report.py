from src.student_app.services.calculator import calculate_grade
def generate_student_report(student):
    grade = calculate_grade(student.marks)
    report = [
        "",
        "Student Report",
        "==============",
        f"ID: {student.student_id}",
        f"Name: {student.name}",
        f"Program: {student.program}",
        f"Semester: {student.semester}",
        f"Marks: {student.marks}",
        f"Grade: {grade}",
    ]
    return "\n".join(report)
