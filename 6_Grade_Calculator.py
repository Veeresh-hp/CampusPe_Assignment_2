try:
    subject_scores = []
    for index in range(1, 6):
        score = float(input(f"Enter marks for Subject {index}: "))
        if score < 0 or score > 100:
            raise ValueError("Marks must be between 0 and 100.")
        subject_scores.append(score)

    total_score = sum(subject_scores)
    percentage_score = total_score / 5

    if percentage_score >= 90:
        grade_letter = "A+"
    elif percentage_score >= 80:
        grade_letter = "A"
    elif percentage_score >= 70:
        grade_letter = "B"
    elif percentage_score >= 60:
        grade_letter = "C"
    elif percentage_score >= 50:
        grade_letter = "D"
    else:
        grade_letter = "F"

    result_status = "Pass" if all(mark >= 40 for mark in subject_scores) else "Fail"

    print("\n--- Academic Result ---")
    print("Total Marks  :", total_score)
    print("Percentage   :", percentage_score)
    print("Grade        :", grade_letter)
    print("Result       :", result_status)

except ValueError as err:
    print("Input Error:", err)