data = []
for i in range(4):
    data.append([int(x) for x in input().strip().split()])
d = int(input())

oria = [0, 0, 0, 3]
orib = [0, 0, 3, 0]
varax = [1, 0, 1, 0]
varay = [0, 1, 0, 1]
varbx = [0, 1, 0, -1]
varby = [1, 0, -1, 0]


def getv(arr, a, b):
    global oria, orib, varax, varbx, varay, varby, d
    return arr[oria[d] + varax[d] * a + varbx[d] * b][orib[d] + varay[d] * a + varby[d] * b]


def setv(arr, a, b, val):
    global oria, orib, varax, varbx, varay, varby
    arr[oria[d] + varax[d] * a + varbx[d] * b][orib[d] + varay[d] * a + varby[d] * b] = val


ans = [[0 for i in range(4)] for j in range(4)]
for i in range(4):
    k = 0
    for j in range(4):
        if k < 4:
            while k < 4:
                kval = getv(data, i, k)
                if kval > 0:
                    break
                k += 1
            if k < 4:
                setv(ans, i, j, kval)
                k += 1
                while k < 4:
                    kval = getv(data, i, k)
                    if kval > 0:
                        break
                    k += 1
                if k < 4 and kval == getv(ans, i, j):
                    setv(ans, i, j, kval * 2)
                    k += 1

for i in ans:
    for j in i:
        print(j, '', end='')
    print()
