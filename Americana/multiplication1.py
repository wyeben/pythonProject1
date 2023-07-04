number = int(input("Enter a number: "))
for i in range(1,number +1):
    print(f"Times table for {i}:")
    for j in range(1, 13):
        product = i * j
        print(f"{i} x {j} = {product}")
    print()
