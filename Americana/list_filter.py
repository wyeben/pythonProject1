y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([i for i in y if i % 2 == 0])
print([n ** 2 for n in y])
print([r**3 for r in y])
print([v/2 for v in y])

print(list(map(lambda x: x ** 2, y)))

def palindrome(n):
    n = n.lower().replace(" ", "")
    return n == n[::-1]

name = "madam"
check = palindrome(name)
print(check)
