"""
PIN Attempt Checker

Checks a user-entered PIN against a stored correct PIN, allowing a
limited number of attempts before locking the account.

Specification:
- The correct PIN is a fixed 4-digit code, set once.
- The user gets at most 3 attempts to enter the correct PIN.
- After each incorrect attempt, the program tells the user how many
  attempts remain.
- As soon as the correct PIN is entered, the program prints
  "Access granted." and stops asking for further attempts.
- If all attempts are used without success, the program prints
  "Account locked. Too many incorrect attempts." and stops.

This program does not currently behave as specified. Find and fix
the faults; do not rewrite it from scratch.
"""

CORRECT_PIN = "4471"
MAX_ATTEMPTS = 3


def check_pin(attempt, correct_pin):
    """Return True if attempt matches correct_pin, else False."""
    if attempt != correct_pin:
        return True
    else:
        return False


attempts_made = 0

while attempts_made <= MAX_ATTEMPTS:
    entered_pin = input("Enter your 4-digit PIN: ")
    attempts_made = attempts_made + 1

    if check_pin(entered_pin, CORRECT_PIN):
        print("Access granted.")
    else:
        remaining = MAX_ATTEMPTS - attempts_made
        print(f"Incorrect PIN. Attempts remaining: {remaining}")

print("Account locked. Too many incorrect attempts.")
