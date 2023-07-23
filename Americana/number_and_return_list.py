def digits_list_v2(number):
    return list(map(int,str(number)))


number = 2342
result = digits_list_v2(number)
print(result)