import random

boys = 0
win = random.randint(1,5)
while boys <= 5:
     lucky = int(input("Try any number to WIN 1000,000:"))
     if lucky == win:
      print("You are our lucky Winner")
      exit()