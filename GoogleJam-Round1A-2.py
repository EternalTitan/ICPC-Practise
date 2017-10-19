import math


def init():
    # fin=open("input.txt","r")
    # global fout
    # fout=open("output.txt",'wb')
    pass


def calc(num, need):
    gt = num / 0.9 / need
    lt = num / 1.1 / need
    d1 = math.ceil(lt)
    d2 = math.floor(gt)
    if d1 <= d2:
        return d1, d2
    else:
        return 0, 0


init()
T = int(input())
for t0 in range(T):
    n, p = [int(x) for x in input().strip().split()]
    req = [int(x) for x in input().strip().split()]
    pac = []
    for i in range(n):
        temp = [int(x) for x in input().strip().split()]
        pac.append(temp)
    calculated = [[0 for j in range(p)] for i in range(n)]
    dic = [{} for j in range(n)]
    counter = [[] for j in range(n)]
    siz = [0 for j in range(n)]
    for i in range(n):
        for j in range(p):
            t1, t2 = calc(pac[i][j], req[i])
            calculated[i][j] = t1
            for temp in range(t1, t2 + 1):
                if temp not in dic[i]:
                    counter[i].append(0)
                    dic[i][temp] = siz[i]
                    siz[i] += 1
                counter[i][dic[i][temp]] += 1
    ans = 0
    for i in dic[0]:
        if i > 0:
            mi = 999
            flag = True
            for j in range(n):
                if i in dic[j]:
                    temp = counter[j][dic[j][i]]
                    if mi > temp:
                        mi = temp
                else:
                    flag = False
                    break
            if flag:
                ans += mi
    print("Case #%d: " % (t0 + 1), ans)
    # fout.close()
