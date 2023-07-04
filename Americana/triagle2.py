for i in range(1, 10):
    for j in range(i):
        print('#', end='')
    print()
print()

for i in range(9, 0, -1):
    for j in range(i):
        print('#', end='')
    print()
print()

for i in range(9, 0, -1):
    for j in range(9 - i):
        print(' ', end='')
    for k in range(i):
        print('#', end='')
    print()
print()

for i in range(1, 10):
    for j in range(9 - i):
        print(' ', end='')
    for k in range(i):
        print('#', end='')
    print()
