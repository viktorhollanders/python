grade_input = 0.0
total_credid = 0
weighted_average_grade = 0
highest_grade = -1

while grade_input >= 0.0:
    grade_input = float(input())

    if grade_input >= 0:
        credid_input = int(input())

        weighted_average_grade += grade_input * credid_input
        total_credid += credid_input

        if grade_input > highest_grade:
            highest_grade = grade_input

if total_credid > 0:
    print(f"Weighted average grade: {round(weighted_average_grade / total_credid, 2)}")

if highest_grade > 0:
    print(f"Highest grade: {highest_grade}")
