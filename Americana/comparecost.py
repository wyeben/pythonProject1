price1 = float(input("enter price for package 1"))
weight = float(input("enter weight for package 1"))
price2 = float(input("enter price for package 2"))
weight = float(input("enter weight for package 2"))

if price1 > price2:
    print("package 2 has a better price")
elif price2 > price1:
    print("package 1 has a better price")
else:
    print("the both have the same price")

