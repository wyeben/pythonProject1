def americana(numbers):
    number = len(numbers)

    for i in range(number - 1):
        for j in range(number - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


unsorted_list = [8, 2, 5, 6, 1, 3, 9, 4, 7]
sort_list = americana(unsorted_list)
print(sort_list)