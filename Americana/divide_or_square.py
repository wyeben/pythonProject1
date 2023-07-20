import math


def divide_or_square(number):
    if number % 5 == 0:
        return math.sqrt(number)
    else:
        return number % 5

numbers = 21
divide = divide_or_square(numbers)
print(divide)