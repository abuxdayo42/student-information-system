import json

from src.student_app.repositories.student_repository import StudentRepository


def test_load_student_data(tmp_path):
    test_file = tmp_path / "student.json"

    test_data = {
        "id": "2024001",
        "name": "Ali",
        "program": "BS Computer Science",
        "semester": 4,
        "marks": 85
    }

    test_file.write_text(json.dumps(test_data))

    repository = StudentRepository(str(test_file))

    result = repository.load()

    assert result == test_data


def test_save_student_data(tmp_path):
    test_file = tmp_path / "student.json"

    repository = StudentRepository(str(test_file))

    test_data = {
        "id": "2024001",
        "name": "Ali",
        "program": "BS Computer Science",
        "semester": 7,
        "marks": 92
    }

    result = repository.save(test_data)

    assert result is True

    saved_data = json.loads(test_file.read_text())

    assert saved_data == test_data


def test_load_missing_file(tmp_path):
    test_file = tmp_path / "missing.json"

    repository = StudentRepository(str(test_file))

    result = repository.load()

    assert result is None