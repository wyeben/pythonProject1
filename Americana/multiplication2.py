number = int(input('enter a number'))
for ben in range(1, 13):
    row = ""
    for ben2 in range(1, number + 1):
     row += "{:4d}".format(ben * ben2)
    print(row)