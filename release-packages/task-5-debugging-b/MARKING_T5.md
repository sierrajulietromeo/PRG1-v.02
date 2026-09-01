# Task 5: Debugging, Part B, Marking Scheme

Companion to `BRIEF_T5.md` | Module code PRG1

20 marks total, 10% of the module assignment: 10 for the fix, 10 for the fault log.

## Part 1: Correctness of the fix, 10 marks

Run `pytest PRG1_Task5_Debugging_test.py -v`. It checks `report.txt` against two different data sets, so a fix that only works for the sample data will not pass.

| Marks | What it shows |
|---|---|
| 10 | All report lines correct, class average recalculates properly for different data, and `report.txt` contains every line. |
| 4-9 | Passes on the original sample data but not the second data set, or the report is missing lines. |
| 0-3 | Most faults still present; report incomplete or badly wrong. |

## Part 2: Fault log quality, 10 marks

| Marks | What it shows |
|---|---|
| 8-10 | All three faults correctly identified and clearly explained, in your own words. |
| 4-7 | Some faults correctly explained; others weak, generic, or just restate the code. |
| 0-3 | Faults not correctly identified, or explanations just restate the code. |
