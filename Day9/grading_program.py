student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
    
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    if 80 < student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    if 70 < student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    if student_scores[key] <= 70:
        student_grades[key] = "Fail"


print(student_grades)

