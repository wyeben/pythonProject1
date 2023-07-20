import random

rock = 0
paper = 1
scissor = 2
game_score = [rock, paper,scissor]

user = int(input("enter (0) for rock (1) paper (3) scissor\n"))
print(game_score[user])

computer_choice = random.randint(0,2)
print(game_score[computer_choice])

if user > computer_choice:
    print(f"{game_score[0]}you win")