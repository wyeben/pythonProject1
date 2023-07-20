def find_largest_element(number):
    largest = number[0]

    for element in number:
        if element > largest:
            largest = element
    return largest

numbers = [10,2,33,4,6,21,7]
largest_element = find_largest_element(numbers)
print("The largest element is:",largest_element)