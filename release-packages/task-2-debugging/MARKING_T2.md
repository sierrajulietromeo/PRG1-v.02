# Task 2: Debugging, Part A, Marking Scheme

Companion to `BRIEF_T2.md` | Module code PRG1

20 marks total, 10% of the module assignment: 10 for the fix, 10 for the fault log.

## Part 1: Correctness of the fix, 10 marks

Run `pytest PRG1_Task2_Debugging_test.py` against your submission. 3 marks per scenario passed exactly as specified (9 marks), plus 1 mark for keeping the original structure (constant, function, loop retained).

| Scenario | Expected result once fixed |
|---|---|
| Correct PIN on first attempt | `"Access granted."` printed once; program ends without asking again. |
| Two wrong PINs, then correct | Attempts remaining shown after each wrong entry, then `"Access granted."` |
| Three wrong PINs | Attempts remaining shown twice, then `"Account locked."` No 4th prompt. |

## Part 2: Fault log quality, 10 marks

| Marks | What it shows |
|---|---|
| 8-10 | All three faults correctly identified and clearly explained, in your own words. |
| 4-7 | Some faults correctly explained; others weak, generic, or just restate the code. |
| 0-3 | Faults not correctly identified, or explanations just restate the code. |
