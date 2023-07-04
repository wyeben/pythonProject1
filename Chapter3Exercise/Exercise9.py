num = int(input("Enter a five-digit integer: "))

for i in range(5):
    digit = (num // (10 ** (4 - i))) % 10
    print("Digit at position", i + 1, ":", digit)