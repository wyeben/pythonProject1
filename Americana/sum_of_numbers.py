def sum_the_numbers(n):
    total = 0
    for number in n:
        total += number
    return total

def sum_of_numbers(n):
    total = 0
    s = 0
    while s < len(n):
        total += n[s]
        s += 1
    return total

def sum_all_numbers(n):
    total = 0
    s = 0
    while True:
        total += n[s]
        s += 1
        if s >= len(n):
            break
    return total

numbers = [1,2,3,4,5]
cal = sum_all_numbers(numbers)
print(cal)