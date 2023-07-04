print("(a)")
for i in range(1, 6):
    for j in range(i):
        print('*', end='')
    print()

print("\n(b)")
for i in range(5, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

print("\n(c)")
for i in range(1, 6):
    for j in range(5 - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

print("\n(d)")
for i in range(5, 0, -1):
    for j in range(5 - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()