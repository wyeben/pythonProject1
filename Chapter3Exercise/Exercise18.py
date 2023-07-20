for asteriks in range(1,10):
    for row in range(asteriks):
        print(f'*',end='')
    print()

print()
for asteriks in range(1,9):
    for row in range(1,4):
        for shape in range(asteriks + row):
            print('*',end='')
        print('',end='')
    print()