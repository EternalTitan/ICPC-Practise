out = open("1.out", "w")
T = int(input())
for t0 in range(T):
    d, n = [int(x) for x in input().strip().split()]
    maxTime = 0
    for i in range(n):
        k, s = [int(x) for x in input().strip().split()]
        temp = (d - k) / s
        if temp > maxTime:
            maxTime = temp
    out.write("Case #" + str(t0 + 1) + ": " + str(d / maxTime) + "\n")
