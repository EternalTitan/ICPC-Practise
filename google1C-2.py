out = open("2.out", "w")
T = int(input())
for t0 in range(T):
    out.write("Case #" + str(t0 + 1) + ": ")
    n, k = [int(x) for x in input().strip().split()]
    u = float(input())
    p = [float(x) for x in input().strip().split()]
    p.sort()

    psum = [0 for i in range(n + 1)]
    psum[0] = p[0]
    for i in range(1, n):
        psum[i] = psum[i - 1] + p[i]

    i = 1
    while i < n and p[i] * (i + 1) - psum[i] < u:
        i += 1

    avg = (u + psum[i - 1]) / i
    for j in range(i):
        p[j] = avg

    ans = 1.0

    for i in p:
        ans *= i
    out.write("%.7f" % ans)

    out.write("\n")
out.close()
