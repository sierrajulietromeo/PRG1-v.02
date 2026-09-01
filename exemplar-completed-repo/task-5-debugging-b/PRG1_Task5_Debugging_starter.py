"""
Student Grade Report

Reads a file of student names and scores, works out whether each
student has passed or failed, and writes a report file summarising
the results.
"""

PASS_MARK = 40


def main():
    with open("scores.txt", "r") as scores_file:
        lines = scores_file.readlines()

    total = 0
    count = 0

    report_file = open("report.txt", "w")

    for line in lines:
        line = line.strip()
        name, score_text = line.split(",")
        score = int(score_text)
        total = total + score
        count = count + 1

        if score >= PASS_MARK:
            status = "Pass"
        else:
            status = "Fail"

        report_file.write(f"{name}: {score} ({status})\n")

    average = total / count

    report_file.write(f"Class average: {average:.1f}\n")
    report_file.close()


if __name__ == "__main__":
    main()
