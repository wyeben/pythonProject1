def remove_duplicate(input_list):
    unique_list = []
    while input_list:
        item = input_list[0]
        unique_list.append(item)
        input_list = [x for x in input_list if x != item]
    return unique_list


list1 = [1, 1, 2, 2, 4, 5, 1, 6, 7, 7, 1, 8, 4]
duplicate = remove_duplicate(list1)
print(duplicate)
