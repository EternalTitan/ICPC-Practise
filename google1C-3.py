out = open("3.out", "w")
T = int(input())
for t0 in range(T):
    out.write("Case #" + str(t0 + 1) + ": ")
    ac, aj = [int(x) for x in input().strip().split()]
    dataA = []
    dataJ = []
    totA = 0
    totJ = 0
    fintv = []
    aintv = []
    jintv = []
    ans = 0
    for i in range(ac):
        dataA.append([int(x) for x in input().strip().split()])
    for i in range(aj):
        dataJ.append([int(x) for x in input().strip().split()])
    for i in range(len(dataA)):
        totA += dataA[i][1] - dataA[i][0] + 1
    for i in range(len(dataJ)):
        totJ += dataJ[i][1] - dataJ[i][0] + 1
    dataA.sort(key=lambda x: x[0])
    dataJ.sort(key=lambda x: x[0])

    i = 0
    j = 0
    lasperson = 0
    lasloc = 0
    fst = -1
    last = -1
    while i < ac or j < aj:
        nxt = 0
        nxtSt = 0
        if i == ac:
            nxt = 2
            nxtSt = dataJ[j][0]
        elif j == aj:
            nxt = 1
            nxtSt = dataA[i][0]
        else:
            if dataA[i][0] < dataJ[j][0]:
                nxt = 1
                nxtSt = dataA[i][0]

            else:
                nxt = 2
                nxtSt = dataJ[j][0]

        if fst == -1:
            fst = nxt
            fstpst = nxtSt
        last = nxt
        if nxt == 1:
            lasend = dataA[i][1]
        else:
            lasend = dataJ[j][1]

        if lasperson == 0:
            lasperson = nxt
        if lasperson != nxt:
            ans += 1
        if nxtSt > lasloc:
            if lasperson == nxt:
                if nxt == 1:
                    aintv.append(nxtSt - lasloc)
                else:
                    jintv.append(nxtSt - lasloc)
            else:
                fintv.append(nxtSt - lasloc)

        if nxt == 1:
            i += 1
        else:
            j += 1

    # if lasloc<1440:
    #     if lasperson==1:
    #         aintv.append(1440-lasloc)
    #     elif lasperson==2:
    #         jintv.append(1440-lasloc)
    #     else:
    #         fintv.append(1440-lasloc)
    if fst != last:
        fintv.append(1440 - lasend + fstpst)
        ans += 1
    aintv.sort()
    jintv.sort()
    fintvtot = sum(fintv)
    needA = 720 - totA
    needJ = 720 - totJ

    while needJ > 0 and len(jintv) > 0:
        if needJ >= jintv[0]:
            needJ -= jintv.pop(0)
        else:
            jintv[0] -= needJ
            needJ = 0

    while needA > 0 and len(aintv) > 0:
        if needA >= aintv[0]:
            needA -= aintv.pop(0)
        else:
            aintv[0] -= needA
            needA = 0

    if needA > 0:
        needA -= min(needA, fintvtot)
        fintvtot -= min(needA, fintvtot)
    if needJ > 0:
        needJ -= min(needJ, fintvtot)
        fintvtot -= min(needJ, fintvtot)

    # aintv.sort(reverse=True)
    # jintv.sort(reverse=True)
    while needA > 0:
        needA -= jintv.pop()
        ans += 1

    while needJ > 0:
        needJ -= aintv.pop()
        ans += 1

    out.write(str(ans))
    out.write("\n")
out.close()
