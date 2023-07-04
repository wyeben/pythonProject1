
total_score = 0
num_students = 20

for i in range(num_students):
    score = int(input("Enter the score for student {}: ".format(i + 1)))
    total_score += score


average_score = total_score / num_students
print("*********************************************************************")
print("              Aso Rock Secondary School, Abuja Nigeria")
print("*********************************************************************")
print("Class: SSS 3")
print("Number of Student in class: 20")
print("Total score:",total_score)
print("Average Score:", average_score)
print("*********************************************************************")
