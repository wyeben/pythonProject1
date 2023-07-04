score = int(input("Enter your score"))
if score >= 80 and score <= 100:
    print("Your score is", score, "Your grade is A")
elif score < 80 and score >= 70:
     print("Your score is", score, "Your grade is B")
elif score < 70 and score >= 55:
     print("Your score is", score, "Your grade is C")
else:
    print("You have failed")