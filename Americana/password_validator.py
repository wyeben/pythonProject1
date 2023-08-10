import re
import sys
import time
import random
import datetime


def generate_password():
    user_input = int(input(f"\n    🌀WELCOME🌀 \n         TO\n        🌀🌀PASSWORD\nGENERATOR🌀\n"
                           f"\nHow many letters would you want?\n"))
    user_input2 = int(input("How many numbers do you want?\n"))
    user_input3 = int(input("How many symbols would you like?\n"))

    alphabets = ['A', 'b', 'C', 'd', 'E', 'f', 'G', 'H', 'i', 'j', 'K',
                 'l', 'M', 'n', 'O', 'p', 'q', 'R', 's', 'T', 'u', 'V',
                 'w', 'x', 'Y', 'z']

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    symbols = ['$', '&', '*', '(', ')', '@', '#', '.', '?',
               '"', ':', '{', '}', '|', '<', '>', '!', '%',
               '^']

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


def draw_progress_bar(iteration, total, bar_length=20):
    percent = iteration / total
    arrow = '🔸''🔹' * int(round(percent * bar_length) - 1)
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write(f'\r[{arrow}{spaces}] {int(percent * 100)}%')
    sys.stdout.flush()


def progress_bar_animation():
    total_iterations = 10
    for i in range(total_iterations + 1):
        draw_progress_bar(i, total_iterations)
        time.sleep(0.5)


def rotating_flag_animation():
    animation_frames = ["🇨🇦", "🇺🇸", "🇦🇽", "🇧🇫", "🇦🇱", "🇧🇸", "🇨🇩", "🇧🇷",
                        "🇦🇶", "🇨🇫", "🇨🇰", "🇬🇭", "🇩🇰", "🇦🇬", "🇳🇬"]

    iterations = 15
    for i in range(iterations):
        sys.stdout.write("\r" + animation_frames[i % len(animation_frames)])
        sys.stdout.flush()
        time.sleep(1)


def validate_password(password):
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")

    if not re.search(r'[a-z]', password):
        errors.append("Password must contain at least one lowercase letter")

    if not re.search(r'[A-Z]', password):
        errors.append("Password must contain at least one uppercase letter")

    if not re.search(r'[0-9]', password):
        errors.append("Password must contain at least one numerical digit")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        errors.append("Password must contain at least one special character")

    if errors:
        print("\nInvalid password. Errors:")
        for error in errors:
            print("🚫 " + error)
        return False
    else:
        print("\nValid password:", password)
        return True


rotating_flag_animation()

the_time = datetime.datetime.now()

print("  NIGERIA   ", the_time)
print()


def password_validator():
    print("    🌀WELCOME🌀 \n         TO\n        🌀🌀PASSWORD\nVALIDATOR🌀\n")
    while True:
        password = input("Enter password to validate or press ( 1⃣ ) to generate a new password:\n")
        print("Loading")
        progress_bar_animation()
        if password == "1":
            new_password = validate_password(generate_password())
            if new_password:
                print("Password meets the criteria 💯 thank you 🤗")
                break
            else:
                print("Password does not meet the criteria 🔴 Please try again🔁")

        elif validate_password(password):
            print("Password meets the criteria 💯 thank you 🤗")
            break
        else:
            print("Password does not meet the criteria🔴 Please try again🔁")


if __name__ == "__main__":
    password_validator()
