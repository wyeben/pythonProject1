number = int(input("Enter a number: "))

divisible_by_5_and_6 = (number % 5 == 0) and (number % 6 == 0)
divisible_by_5_or_6 = (number % 5 == 0) or (number % 6 == 0)
divisible_by_5_or_6_but_not_both = divisible_by_5_or_6 and not divisible_by_5_and_6

print("Divisible by 5 and 6:", divisible_by_5_and_6)
print("Divisible by 5 or 6:", divisible_by_5_or_6)
print("Divisible by 5 or 6, but not both:", divisible_by_5_or_6_but_not_both)