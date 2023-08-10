import random

from Americana.password_validator import progress_bar_animation, validate_password


def generate_password():
    user_input = int(input(f"Welcome to password generator:\n"
                           f"How many letters would you want?\n"))
    user_input2 = int(input("How many numbers do you want?\n"))
    user_input3 = int(input("How many symbols would you like?\n"))

    alphabets = ['A', 'b', 'C', 'd', 'E', 'f', 'G', 'H', 'i', 'j', 'K',
                 'l', 'M', 'n', 'O', 'p', 'q', 'R', 's', 'T', 'u', 'V',
                 'w', 'x', 'Y', 'z']

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    symbols = ['$', '&', '*', '(', ')', '@', '#']

    password_list = []

    for elem in range(1, user_input + 1):
        password_list += random.choice(alphabets)

    for elem in range(user_input2):
        password_list += random.choice(numbers)

    for elem in range(user_input3):
        password_list += random.choice(symbols)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    return password



