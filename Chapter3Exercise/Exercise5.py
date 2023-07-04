print('Enter two integers, and I will tell you','the relationships they satisfy.')
number1 = int(input('Enter first integer: '))

number2 = int(input('Enter second integer: '))

if number1 == number2:
    print(f'number: {number1} is equal to {number2}')
elif number1 != number2:
    print(f'number: {number1} is not equal to {number2}')
else:
    print(f'number: {number1} is equal to {number2}')