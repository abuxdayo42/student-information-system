from src.student_app.utils.validation import get_valid_marks, get_valid_semester


def test_valid_marks(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "85")

    result = get_valid_marks()

    assert result == 85


def test_invalid_then_valid_marks(monkeypatch):
    inputs = iter(["150", "92"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_valid_marks()

    assert result == 92


def test_valid_semester(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "7")

    result = get_valid_semester()

    assert result == 7


def test_invalid_then_valid_semester(monkeypatch):
    inputs = iter(["10", "5"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_valid_semester()

    assert result == 5