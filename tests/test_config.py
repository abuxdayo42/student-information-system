from src.student_app.config import APP_NAME, DEBUG, MAX_STUDENTS


def test_app_name():
    assert APP_NAME == "Student Information System"


def test_debug_is_boolean():
    assert isinstance(DEBUG, bool)


def test_max_students_is_integer():
    assert isinstance(MAX_STUDENTS, int)


def test_max_students_value():
    assert MAX_STUDENTS == 100