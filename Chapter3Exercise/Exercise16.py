largest = float('-inf')
second_largest = float('-inf')

for i in range(10):
    number = float(input("Enter a number: "))

    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number

print("The largest number is:", largest)
print("The second largest number is:", second_largest)