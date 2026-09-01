"""
Automated checks for Task 2: Debugging, Part A (PIN Attempt Checker).

Run with: pytest PRG1_Task2_Debugging_test.py

These tests run the submitted PRG1_Task2_Debugging_starter.py as a
separate process and check its output against the specification given
in the Task 2 brief. They are the same three scenarios students are
told to test themselves, so a submission that follows the brief's own
advice should already pass.

The tests do not import or inspect the code directly, only its
printed output, so any correct fix passes regardless of how it was
implemented (a break statement, a flag variable, or any other valid
approach).
"""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent / "PRG1_Task2_Debugging_starter.py"


def run_program(pin_entries):
    """Run the starter script, feeding it the given PIN entries as stdin.

    Returns the combined stdout produced by the program.
    """
    stdin_text = "\n".join(pin_entries) + "\n"
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=stdin_text,
        capture_output=True,
        text=True,
        timeout=5,
    )
    return result.stdout


def test_script_exists():
    assert SCRIPT.exists(), (
        f"Expected to find {SCRIPT.name} in the same folder as this test file."
    )


def test_correct_pin_first_attempt():
    """Entering the correct PIN straight away should grant access and stop."""
    output = run_program(["4471"])
    assert "Access granted." in output
    assert output.count("Enter your 4-digit PIN") == 1, (
        "Program should not ask for a further PIN after granting access."
    )
    assert "Account locked" not in output


def test_two_wrong_then_correct():
    """Two wrong PINs, then the correct one, should grant access on the third try."""
    output = run_program(["0000", "1111", "4471"])
    assert "Attempts remaining: 2" in output
    assert "Attempts remaining: 1" in output
    assert "Access granted." in output
    assert "Account locked" not in output


def test_three_wrong_locks_account():
    """Three wrong PINs in a row should lock the account, with no fourth prompt."""
    output = run_program(["0000", "1111", "2222"])
    assert "Attempts remaining: 2" in output
    assert "Attempts remaining: 1" in output
    assert "Attempts remaining: 0" in output
    assert "Account locked. Too many incorrect attempts." in output
    assert "Access granted." not in output
    assert output.count("Enter your 4-digit PIN") == 3, (
        "Program should stop after exactly 3 attempts, not offer a 4th."
    )


if __name__ == "__main__":
    import pytest
    sys.exit(pytest.main([__file__, "-v"]))
