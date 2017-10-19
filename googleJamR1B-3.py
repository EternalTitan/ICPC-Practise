out = open("3.out", "w")
T = int(input())
for t0 in range(T):
    n, q = [int(x) for x in input().strip().split()]
    horse = []
    for i in range(n):
        horse.append([int(x) for x in input().strip().split()])
    disTo = [0]
    for i in range(n):
        temp = [int(x) for x in input().strip().split()]
        if i < n - 1:
            disTo.append(temp[i + 1])
    input()
    tim = [9999999999999 for i in range(n + 2)]
    tim[0] = 0
    for i in range(n - 1):
        remainDis = horse[i][0]
        for j in range(i + 1, n):
            if disTo[j] > remainDis:
                break
            remainDis -= disTo[j]
            timeUsed = (horse[i][0] - remainDis) / horse[i][1]
            if tim[j] > tim[i] + timeUsed:
                tim[j] = tim[i] + timeUsed
    out.write("Case #" + str(t0 + 1) + ": ")
    out.write(str(tim[n - 1]) + "\n")
out.close()
