# Task 5: Debugging, Part B, Answers

Complete this alongside `BRIEF_T5.md`.

## Fault log

### Fault 1

**What was wrong, and where**

> The line from `scores.txt` wasn't stripped before being split, so `score_text` still had the newline character on the end of it.

**Why it caused incorrect behaviour, and how you fixed it**

> This meant the newline ended up embedded in the middle of the written report line, so instead of one clean line it printed something broken across two lines. I fixed it by calling `.strip()` on the line before splitting it, and I also changed the write to use the converted `score` number instead of the raw `score_text`, so there's no chance of a leftover newline either way.

### Fault 2

**What was wrong, and where**

> `average = total / NUM_STUDENTS`, where `NUM_STUDENTS` was a fixed constant set to 4.

**Why it caused incorrect behaviour, and how you fixed it**

> If the data file doesn't have exactly 4 students in it, dividing by a fixed number of 4 gives the wrong average, for example with 5 students it divides by too small a number and the average comes out too high. I fixed it by dividing by `count`, which counts how many students were actually processed in the loop, and removed `NUM_STUDENTS` since it wasn't needed any more.

### Fault 3

**What was wrong, and where**

> `report.txt` was being opened in `"w"` mode inside the loop, once per student, and then opened in `"w"` mode again after the loop for the class average line.

**Why it caused incorrect behaviour, and how you fixed it**

> Opening a file in `"w"` mode wipes it completely every time it's opened, so each new student line was deleting the one written before it, and then the final open for the average line wiped out all the student lines too, leaving only the average in the file. I fixed it by opening the file once before the loop starts, writing every student line and the class average line to that same open file, then closing it once at the very end.
