import math

out = open("1.out", "w")
T = int(input())
for t0 in range(T):
    out.write("Case #" + str(t0 + 1) + ": ")
    n, k = [int(x) for x in input().strip().split()]
    data = []
    for i in range(n):
        data.append([int(x) for x in input().strip().split()])

    data.sort(key=lambda x: x[1], reverse=True)
    data.sort(key=lambda x: x[0], reverse=True)
    # print(data)

    ans = [[0 for i in range(1002)] for j in range(1002)]

    for i in range(n):
        ans[i][1] = math.pi * data[i][0] * data[i][0] + 2 * math.pi * data[i][0] * data[i][1]
        if i > 0 and ans[i][1] < ans[i - 1][1]:
            ans[i][1] = ans[i - 1][1]
        for j in range(2, k + 1):
            ans[i][j] = ans[i - 1][j - 1] + 2 * math.pi * data[i][0] * data[i][1]
            temp = 0
            if i > 0:
                temp = ans[i - 1][j]
            if temp > ans[i][j]:
                ans[i][j] = temp
            temp = ans[i][j - 1]
            if ans[i][j] < temp:
                ans[i][j] = temp
    # print(ans[n-1][k])
    out.write("%.9f" % ans[n - 1][k])

    out.write("\n")
out.close()
