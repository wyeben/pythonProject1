def greater(number1, number2, number3, number4):
    maximum = number1
    if number2 > maximum:
        maximum = number2
    if number3 > maximum:
        maximum = number3
    if number4 > maximum:
        maximum = number4
    print(maximum)
greater(6,0,7,8)
