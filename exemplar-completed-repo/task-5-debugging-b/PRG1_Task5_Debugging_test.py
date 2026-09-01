"""
Automated checks for Task 5: Debugging, Part B (Student Grade Report).

Run with: pytest PRG1_Task5_Debugging_test.py

Place the submitted, corrected PRG1_Task5_Debugging_starter.py in the
same folder as this test file before running. Each test runs the
program in its own temporary folder with a fresh scores.txt, so
different tests can check the program against different data without
interfering with each other, and without needing scores.txt from the
original task materials to be present or unmodified.
"""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT_NAME = "PRG1_Task5_Debugging_starter.py"
SCRIPT_PATH = Path(__file__).parent / SCRIPT_NAME

SAMPLE_SCORES = (
    "Aisha Khan,72\n"
    "Tom Wright,38\n"
    "Priya Patel,55\n"
    "Jamal Osei,91\n"
    "Chloe Bennett,64\n"
)


def run_program(scores_text):
    """Run the starter script in a fresh temporary folder containing the
    given scores.txt. Returns the contents of report.txt, or an empty
    string if no report.txt was produced.
    """
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        shutil.copy(SCRIPT_PATH, tmp_path / SCRIPT_NAME)
        (tmp_path / "scores.txt").write_text(scores_text)
        subprocess.run(
            [sys.executable, SCRIPT_NAME],
            cwd=tmp_path,
            capture_output=True,
            text=True,
            timeout=5,
        )
        report_path = tmp_path / "report.txt"
        if report_path.exists():
            return report_path.read_text()
        return ""


def test_script_exists():
    assert SCRIPT_PATH.exists(), (
        f"Expected to find {SCRIPT_PATH.name} in the same folder as this test file."
    )


def test_report_has_one_line_per_student():
    output = run_program(SAMPLE_SCORES)
    student_lines = [
        line for line in output.splitlines()
        if line.strip() and not line.startswith("Class average")
    ]
    assert len(student_lines) == 5, (
        f"Expected 5 student lines in report.txt, found {len(student_lines)}. "
        f"report.txt contained:\n{output}"
    )


def test_each_student_line_is_correct():
    output = run_program(SAMPLE_SCORES)
    assert "Aisha Khan: 72 (Pass)" in output
    assert "Tom Wright: 38 (Fail)" in output
    assert "Priya Patel: 55 (Pass)" in output
    assert "Jamal Osei: 91 (Pass)" in output
    assert "Chloe Bennett: 64 (Pass)" in output


def test_class_average_correct_for_sample_data():
    output = run_program(SAMPLE_SCORES)
    assert "Class average: 64.0" in output


def test_class_average_recalculates_for_different_data():
    # A different number of students and scores to the sample data,
    # to catch an average computed with a hardcoded number of students.
    different_scores = "Sam Lee,50\nRiya Shah,90\n"
    output = run_program(different_scores)
    assert "Sam Lee: 50 (Pass)" in output
    assert "Riya Shah: 90 (Pass)" in output
    assert "Class average: 70.0" in output


if __name__ == "__main__":
    import pytest
    sys.exit(pytest.main([__file__, "-v"]))
