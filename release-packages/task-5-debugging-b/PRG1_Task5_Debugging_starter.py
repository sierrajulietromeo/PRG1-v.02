"""
Student Grade Report

Reads a file of student names and scores, works out whether each
student has passed or failed, and writes a report file summarising
the results.

Specification:
- Read every line of scores.txt. Each line is a name and a score,
  separated by a comma, for example: Aisha Khan,72
- A score of 40 or more is a Pass. Below 40 is a Fail.
- For each student, write one line to report.txt in the form:
  Name: Score (Pass)   or   Name: Score (Fail)
- After every student has been written, add one more line to
  report.txt: Class average: XX.X, the true average of every score
  in scores.txt, to one decimal place.
- report.txt should end up with one line per student, in the same
  order as scores.txt, followed by the class average line. Nothing
  should be missing and nothing should be overwritten.

This program does not currently behave as specified. Find and fix
the faults; do not rewrite it from scratch.
"""

PASS_MARK = 40
NUM_STUDENTS = 4


def main():
    with open("scores.txt", "r") as scores_file:
        lines = scores_file.readlines()

    total = 0
    count = 0

    for line in lines:
        name, score_text = line.split(",")
        score = int(score_text)
        total = total + score
        count = count + 1

        if score >= PASS_MARK:
            status = "Pass"
        else:
            status = "Fail"

        report_file = open("report.txt", "w")
        report_file.write(f"{name}: {score_text} ({status})\n")
        report_file.close()

    average = total / NUM_STUDENTS

    report_file = open("report.txt", "w")
    report_file.write(f"Class average: {average:.1f}\n")
    report_file.close()


if __name__ == "__main__":
    main()
