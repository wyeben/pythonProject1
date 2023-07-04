total_score = 0
num_students = 0

while True:
    score = input("Enter score for a student or 't' to terminate: ")
    if score.lower() == 't':
        break

    total_score += int(score)
    num_students += 1

average_score = total_score / num_students if num_students > 0 else 0

print("*********************************************************************")
print("              Aso Rock Secondary School, Abuja Nigeria")
print("*********************************************************************")
print("Class: SSS 3")
print("Number of Student in class:", num_students)
print("Total score:",total_score)
print("Average Score:", average_score)
print("*********************************************************************")
