print("welcome to love calculator")
name1 = input("enter your name")
name2 = input("enter his or her name")

combine_names = name1 + name2
small_letters = combine_names.lower()

t = small_letters.count('t')
r = small_letters.count('r')
u = small_letters.count('u')
e = small_letters.count('e')

true = t + r + u + e


l = small_letters.count('l')
o = small_letters.count('o')
v = small_letters.count('v')
e = small_letters.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score <10 or love_score <90:
    print(f"you love score is: {love_score} : your partner is cheating on you")
elif love_score <= 40 and love_score <= 50:
    print(f'your love score is:{love_score} : you have a good lover')
else:
    print(f"your love score is:{love_score} : keep searching love have not found you yet")