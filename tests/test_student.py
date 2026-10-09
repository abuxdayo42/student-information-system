from src.student_app.models.student import Student


def test_student_creation():
    student = Student(
        "2024001",
        "Ali",
        "BS Computer Science",
        4,
        85
    )

    assert student.student_id == "2024001"
    assert student.name == "Ali"
    assert student.program == "BS Computer Science"
    assert student.semester == 4
    assert student.marks == 85


def test_update_marks():
    student = Student(
        "2024001",
        "Ali",
        "BS Computer Science",
        4,
        85
    )

    student.update_marks(92)

    assert student.marks == 92


def test_update_semester():
    student = Student(
        "2024001",
        "Ali",
        "BS Computer Science",
        4,
        85
    )

    student.update_semester(7)

    assert student.semester == 7


def test_student_status_pass():
    student = Student("101", "Ali", "BSCS", 4, 75)
    assert student.get_status() == "Pass"


def test_student_status_fail():
    student = Student("102", "Ahmed", "BSCS", 4, 40)
    assert student.get_status() == "Fail"