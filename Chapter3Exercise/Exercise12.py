number = input("Enter a five-digit integer: ")

if len(number) != 5 or not number.isdigit():
    print("Invalid input. Please enter a five-digit integer.")
else:
    number = int(number)

    digit1 = number // 10000
    digit2 = (number // 1000) % 10
    digit3 = (number // 100) % 10
    digit4 = (number // 10) % 10
    digit5 = number % 10

    if digit1 == digit5 and digit2 == digit4:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")