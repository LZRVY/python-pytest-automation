from src.log_utils import line_parser
import pytest

def test_valid_line():
    timestamp, level, severity, message = line_parser("20260306-125950|DEBUG:5|This is a debug message")
    assert timestamp == "20260306-125950"
    assert level == "DEBUG"
    assert severity == 5
    assert message == "This is a debug message"

def test_invalid_line():
    with pytest.raises(ValueError):
        line_parser("20260306-125950")

def test_extra_space_parses():
    timestamp, level, severity, message = line_parser("20260306-125950  |   INFO:4   |    This is a info message   ")
    assert timestamp == "20260306-125950"
    assert level == "INFO"
    assert severity == 4
    assert message == "This is a info message"

def test_empty_message_parses():
    with pytest.raises(ValueError, match = "cannot be empty"):
        line_parser("20260306-125950 | DhunDhun |    ")

def test_too_many_fields():
    with pytest.raises(ValueError):
        line_parser("20260306-125950 | INFO | Hello | Extra")