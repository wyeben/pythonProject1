number1 = int(input("enter number 1:"))
number2 = int(input("enter number 2:"))
number3 = int(input('enter number 3:'))
number4 = int(input('enter number 4:'))

maximum = number1
minimum = 0

if number2 > number1:
    maximum = number2
if number3 > maximum:
    maximum = number3
if number4 > maximum:
    maximum = number4


sum = maximum + minimum

print(f"maximum is : {maximum},minimum is : {minimum},sum is : {sum}")