n = int(input())
for c in range(n):
    data = [int(x) for x in list(input())]
    dataSize = len(data)
    loc = -1
    for i in range(dataSize - 1):
        if (data[i] > data[i + 1]):
            loc = i
            break
    print('Case #', c + 1, ': ', sep='', end='')
    if loc == -1:
        for i in data:
            print(i, end='')
        print()
    else:
        tempLoc = loc
        while tempLoc > 0 and data[tempLoc] == data[tempLoc - 1]:
            tempLoc -= 1
        for i in range(tempLoc):
            print(data[i], end='')
        if data[tempLoc] > 1:
            print(data[tempLoc] - 1, end='')
        for i in range(tempLoc + 1, dataSize):
            print(9, end='')
        print()
