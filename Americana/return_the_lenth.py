def return_the_size(n):
    elem = 0
    for t in n:
        elem += 1
    return elem


list1 = [4, 8, 8, 6, 7, 8,6]
result = return_the_size(list1)
print(result)
