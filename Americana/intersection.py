def find_intersection(lst1, lst2):
    return tuple([i for i in lst1 if i in lst2])


list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [42, 30, 80, 65, 68, 88, 95]
result = find_intersection(list1, list2)
print(result)
