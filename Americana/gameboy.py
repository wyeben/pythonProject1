import random

num = 0
won = random.randint(1, 8)
while num <= 8:
    guess = int(input("Enter any number to win:"))
    if guess == won:
        print("You won")
        exit()


