from functools import reduce

sum_numbers = lambda numbers: reduce(lambda x, y: x + y, numbers)

average_numbers = lambda numbers: sum_numbers(numbers) / len(numbers)

product_numbers = lambda numbers: reduce(lambda x, y: x * y, numbers)

smallest_number = lambda numbers: reduce(lambda x, y: x if x < y else y, numbers)

largest_number = lambda numbers: reduce(lambda x, y: x if x > y else y, numbers)

numbers = []

for i in range(4):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

sum_of_numbers = sum_numbers(numbers)
average_of_numbers = average_numbers(numbers)
product_of_numbers = product_numbers(numbers)
smallest_num = smallest_number(numbers)
largest_num = largest_number(numbers)

print("Sum of the numbers:", sum_of_numbers)
print("Average of the numbers:", average_of_numbers)
print("Product of the numbers:", product_of_numbers)
print("Smallest number:", smallest_num)
print("Largest number:", largest_num)
