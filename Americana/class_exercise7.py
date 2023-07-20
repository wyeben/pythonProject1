# def reverse_list(numbers):
#     start = 0
#     end = len(numbers) - 1
#
#     while start < end:
#         numbers[start], numbers[end] = numbers[end], numbers[start]
#         start += 1
#         end -= 1
#
#     return numbers
#
# numbers = [8, 2, 5, 6, 1, 3, 9, 4, 7]
# reversed_numbers = reverse_list(numbers)
# print(reversed_numbers)


# numbers = [8, 2, 5, 6, 1, 3, 9, 4, 7]
# print(numbers[::-1])

ls = [2,4,5,77,8,12,9]
result = [i for i in ls if i % 2 == 0]
print(result)
