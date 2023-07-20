def total_of_a_list(n):
    total = 0
    for num in n:
        total += num
    return total

numbers = [1,12,3,4,5]
calculate_total = total_of_a_list(numbers)
print("total in the list is:",calculate_total)