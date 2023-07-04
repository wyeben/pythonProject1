num = int(input('enter a number'))
for x in range(1, 13):
    row = ''
    for r in range(1, num +1):
        row += '{:4d}'.format(x * r)
    print(row)
