def reverse(lst):
    number = lst[0]

    for number in lst:
        number = lst[::-1]

    return number

numbers = [1,2,3,4,5]
reverse_number = reverse(numbers)
print(reverse_number)