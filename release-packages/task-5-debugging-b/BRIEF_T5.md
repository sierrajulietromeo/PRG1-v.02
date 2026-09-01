# Task 5: Debugging, Part B

Worth 10% of the module assignment | Individual work | Module code PRG1

## What you're doing

`PRG1_Task5_Debugging_starter.py` is meant to read a file of student names and scores, work out who has passed and who has failed, and write a summary report to a second file. It does not currently work correctly.

This is the second debugging task in the module. It follows the same process as Task 2, but at increased difficulty, and now involves reading from and writing to files. It contains three separate faults. Find all three, fix them so the program matches the specification below, and complete the fault log.

Fix the faults directly in the code. Do not rewrite the program from scratch.

A sample data file, `PRG1_Task5_scores.txt`, is provided alongside the starter code. The program expects a file named `scores.txt` in the same folder it is run from; rename or copy the sample file before running it.

## Specification

- Read every line of `scores.txt`. Each line is a name and a score, separated by a comma, for example: `Aisha Khan,72`
- A score of 40 or more is a Pass. Below 40 is a Fail.
- For each student, write one line to `report.txt` in the form: `Name: Score (Pass)`, or `Name: Score (Fail)`.
- After every student has been written, add one more line to `report.txt`: `Class average: XX.X`, the true average of every score in `scores.txt`, to one decimal place.
- `report.txt` should end up with one line per student, in the same order as `scores.txt`, followed by the class average line. Nothing should be missing and nothing should be overwritten.

## Test it yourself

Run the program against the sample data file and open `report.txt` afterwards. With the sample data provided, you should see one correctly formatted line for each of the five students, followed by a class average of 64.0. Try changing the contents of `scores.txt`, for example removing a student or changing a score, and check the report updates correctly, rather than staying fixed at old values.

## Fault log

For each of the three faults: say what was wrong and where in the code it was, then explain why it caused the program to behave incorrectly and how you fixed it. Write in your own words in `ANSWERS_T5.md`.

## If you used an AI tool

AI tool use on this task does not need to be logged separately. At the end of the module you will complete one short reflection, `PRG1_AI_Use_Reflection`, covering AI use across the whole assignment. It is mandatory to submit, but not marked.

## Submission

Submit your corrected `PRG1_Task5_Debugging_starter.py` file alongside `ANSWERS_T5.md`. Do not submit `report.txt` or `scores.txt`; the marking process uses its own data files.
