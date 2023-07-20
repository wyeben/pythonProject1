def highest_odd_number(n):
    highest_odd = 0

    for num in n:
        if num % 2 == 1:
            if highest_odd == 0 or num > highest_odd:
                highest_odd = num

    return highest_odd


numbers_list = [10, 7, 22, 13, 15, 81]
result = highest_odd_number(numbers_list)
print("Highest odd number:", result)


def highest_odd_number(n):
    return max((num for num in n if num % 2 == 1), default=0)


numbers_list = [10, 7, 22, 13, 15, 11]
result = highest_odd_number(numbers_list)
print("Highest odd number:", result)

set1 = {10,7,9,(1,2,2,3),3,2,4,(5,2,2),(5,2,2)}
set2 = {2,3,5,7,9,10,3,6,7}
set1.discard(3)
print(set1)
