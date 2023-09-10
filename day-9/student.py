student_scores = {
    "venerita":85,
    "gina":90,
    "lucas":95,
    "brandon":80,
    "perkins":70,
    "perez":65,
    "ojong":55,
    "herbert":40
}

#METHOD 1
""" student_grades = {}

for grades in student_scores:
    if student_scores[grades] > 90:
        student_grades = grades
        #print(student_grades)
        print(f"{student_grades} that is Outstanding")
    elif student_scores[grades] > 80 and student_scores[grades] <= 90:
        student_grades = grades
        print(f"{student_grades} exceeds expectation")
    elif student_scores[grades] > 70 and student_scores[grades] <= 80:
        student_grades = grades
        print(f"{student_grades} Acceptable")
    elif student_scores[grades] <= 70:
        student_grades = grades
        print(f"{student_grades} fails")
    else:
        print("dismissed") """
        
    #print(student_scores[grades])

#METHOD 2  
student_grades = {}

for students in student_scores:
    score = student_scores[students]
    #print(student_scores[students])
    if score > 90:
        student_grades[students] = 'Outstanding'
    elif score > 80 and score <= 90:
        student_grades[students] = 'Exceeds Expectation'
    elif score > 70 and score <= 80:
        student_grades[students] = 'Acceptable'
    elif score <= 70:
        student_grades[students] = 'Fail'
    else:
        print("dismissed")
print(student_grades)