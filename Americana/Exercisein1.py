x = 2
def number():
    global x
    x+=1
    return x

print(number())
print(number())
number()