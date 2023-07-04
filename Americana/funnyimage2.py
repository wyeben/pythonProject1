def you(usd):
    result = ''
    for num in usd:
        if num == 0:
            result += ' '
        elif num == 1:
            result += '*'
    return result

pis = [
    [0,0,1,1,1,1,0,0],
    [0,1,0,0,0,0,1,0],
    [0,1,0,0,0,0,1,0],
    [0,1,0,0,0,0,1,0],
    [0,0,1,1,1,1,0,0]
]

for pis in pis:
    sss = you(pis)
    print(sss)