def ben(x):
    for i in range(1,13):
       row = ''
       for j in range(1, x +1):
         row += '{:4d}'.format(i*j)
         print(f"{i}*{j}={i*j:<25}\t",end="")
       print()
ben(100)