# Task 2: Debugging, Part A

Worth 10% of the module assignment | Individual work | Module code PRG1

## What you're doing

The file `PRG1_Task2_Debugging_starter.py` is meant to be a PIN attempt checker: a small program that checks a user-entered PIN against a stored correct PIN, giving a limited number of attempts before locking the account. It does not currently work correctly.

It contains three separate faults. Your job is to find all three, fix them so the program matches the specification below, and complete the fault log explaining what was wrong and why.

Fix the faults directly in the code. Do not rewrite the program from scratch: the overall structure (the constant, the `check_pin` function, and the loop) is correct and should stay as it is.

## Specification

- The correct PIN is a fixed 4-digit code, set once, and does not change during a run.
- The user gets at most 3 attempts to enter the correct PIN.
- After each incorrect attempt, the program tells the user how many attempts remain.
- As soon as the correct PIN is entered, the program prints `"Access granted."` and stops asking for further attempts.
- If all 3 attempts are used without success, the program prints `"Account locked. Too many incorrect attempts."` and stops.

## Test it yourself

Run the program and try these three scenarios. All three should match the specification above once your fixes are correct.

- Enter the correct PIN, `4471`, on your first attempt. The program should grant access immediately, without asking again.
- Enter two wrong PINs, then the correct one. The program should show attempts remaining after each wrong entry, then grant access on the third try.
- Enter three wrong PINs. The program should show attempts remaining after the first two, then lock the account after the third, without offering a fourth attempt.

## Fault log

For each of the three faults: say what was wrong and where in the code it was, then explain why it caused the program to behave incorrectly and how you fixed it. Write in your own words in `ANSWERS_T2.md`.

## If you used an AI tool

AI tool use on this task does not need to be logged separately. At the end of the module you will complete one short reflection, `PRG1_AI_Use_Reflection`, covering AI use across the whole assignment. It is mandatory to submit, but not marked.

## Submission

Submit your corrected `PRG1_Task2_Debugging_starter.py` file alongside `ANSWERS_T2.md`.
