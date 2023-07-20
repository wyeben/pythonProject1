numbers = [10, 20, 30, 40, 50]

squared_numbers = [num ** 2 for num in numbers]

lowest = min(squared_numbers)
highest = max(squared_numbers)

difference = highest - lowest

print(squared_numbers)
print("Difference between lowest and highest:", difference)