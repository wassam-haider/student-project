from student_app.utils.validation import validate_name
from student_app.utils.validation import validate_marks


def test_valid_name():
    assert validate_name("Ali") is True


def test_empty_name():
    assert validate_name("") is False


def test_spaces_only_name():
    assert validate_name("   ") is True


def test_valid_marks():
    assert validate_marks(85) is True


def test_negative_marks():
    assert validate_marks(-10) is False


def test_marks_above_limit():
    assert validate_marks(150) is False


def test_marks_lower_boundary():
    assert validate_marks(0) is True


def test_marks_upper_boundary():
    assert validate_marks(100) is True