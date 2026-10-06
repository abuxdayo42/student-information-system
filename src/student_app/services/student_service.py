from src.student_app.models.student import Student
from src.student_app.repositories.student_repository import StudentRepository


repository = StudentRepository("data/student.json")


def load_student():
    data = repository.load()

    if data is None:
        return None

    try:
        student = Student(
            data["id"],
            data["name"],
            data["program"],
            data["semester"],
            data["marks"]
        )

        return student

    except KeyError as error:
        print(f"Error: Missing student field: {error}")
        return None


def save_student(student):
    data = {
        "id": student.student_id,
        "name": student.name,
        "program": student.program,
        "semester": student.semester,
        "marks": student.marks
    }

    return repository.save(data)