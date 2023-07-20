def concatenate_two_list(n,x):
        n += x
        return n

list1 = ["a","b","c"]
list2 = list([1,2,3,])
check = concatenate_two_list(list1,list2)
print(f"[{','.join(map(str, check))}]")
