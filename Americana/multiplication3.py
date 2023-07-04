def ben(x):
 number = int(input("enter any number from 1 to 100"))
 for i in range(1,13):
    row = ''
    for j in range(1, number +1):
         row += '{:4d}'.format(i*j)
         print(f"{i}*{j}={i*j:<25}\t",end="")
    print()