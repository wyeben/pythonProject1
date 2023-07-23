def combine_alternately(list1, list2):
    return [elem for pair in zip(list1, list2) for elem in pair]



list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
result = combine_alternately(list1, list2)
print(f"[{','.join(map(str, result))}]")