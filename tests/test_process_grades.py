import pytest
from src.grades_process import parse_grades, process_grades

def test_parse_valid_line():
    name, score = parse_grades("Vyom,88")
    assert name == "Vyom"
    assert score == 88

def test_parse_extra_spaces():
    name, score = parse_grades("  Vyom    , 89")
    assert name == "Vyom"
    assert score == 89

def test_parse_missing_comma_raises():
    with pytest.raises(ValueError):
        parse_grades("Vyom 88")

def test_parse_non_int_score_raises():
    with pytest.raises(ValueError):
        parse_grades("Vyom, abc")

def test_parse_out_of_range_raises():
    with pytest.raises(ValueError):
        parse_grades("Vyom, 111")

def test_process_grades_pipeline(tmp_path):
    input_path = tmp_path / "grades.txt"
    passed_path = tmp_path / "passed_grades.txt"
    failed_path = tmp_path / "failed_grades.txt"
    invalid_path = tmp_path / "gd_err.txt"

    lines = [
        "Saoirse Conrad, 91",
        "Dilan Wolf, 89",
        "Leighton Kramer, 70",
        "Soren Petty, 37",
        "Ronan Boyer, 15",
        "Kiara, 58",
        "Ronald, N/A",
        "Dan, -15", # - at least 1 invalid line (abc or 105)
    ]
    input_path.write_text("\n".join(lines) + "\n")

    # TODO: call process_grades on this input_path
    summary = process_grades(str(input_path), str(passed_path), str(failed_path), str(invalid_path))

    # TODO: assert summary counts + topper + average
    assert summary["grades parsed"] == 8
    assert summary["pass_count"] == 3
    assert summary["fail_count"] == 3
    assert summary["top-scorer"] == 91
    assert summary["average score of valid entries"] == 60