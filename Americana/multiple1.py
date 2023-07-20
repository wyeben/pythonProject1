def main():
    sum1(10)
    sum1(20)
    sum1(30)
    sum1(number)
    sum2()
    greater(4, 6)


number = int(input('Enter a number'))


def sum1(number):
    total = 0
    for counter in range(1, number + 1):
        total += counter
    print(total)


def sum2():
    total = 0
    for counter2 in range(1, 11):
        total += counter2
    print(total)


def greater(number1, number2):
    maximum = number1
    if number2 > number1:
        maximum = number2
    print(maximum)

main()
print(greater(2, 5))
