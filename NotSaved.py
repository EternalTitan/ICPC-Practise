name = ["b", "I", "M", "N"]
transName = ["Gon", "KAy", "Tra", "Vap"]
ordA = []
Dord = []
transT = []
usedA = set()
usedT = set()
usedD = set()
tot = 0


def judge():
    global ordA, Dord, transT, tot
    tot += 1
    if ordA[1] == 0 or ordA[1] == 3:
        return
    for i in range(4):
        if ordA[i] == Dord[i]:
            return

    for i in range(4):
        if transT[i] == "Gon":
            if Dord[i] == 3 or ordA[i] == 0:
                return

    for i in range(4):
        if transT[i] == "KAy":
            for j in range(4):
                if ordA[j] == 3:
                    if Dord[i] + 1 != Dord[2] or Dord[2] + 1 != Dord[j]:
                        return

    if transT[3] == "Tra" or Dord[3] == 0:
        return

    for i in range(4):
        if ordA[i] == 1:
            if Dord[0] >= Dord[i]:
                return

    for i in range(4):
        if transT[i] == "Vap":
            if ordA[i] + 1 != ordA[0]:
                return

    # if Dord[3]==3:
    #     return

    # for i in range(4):
    #     if Dord[i]==3:
    #         if i!=3:
    #
    #             for j in range(4):
    #                 if transT[j]=="Tra":
    #                     if ordA[i]+1!=ordA[j]:
    #                         return


    print(Dord)
    print(transT)
    print(ordA)


def dfsA(k):
    global usedA, ordA
    if k == 0:
        judge()
    else:
        for i in range(4):
            if i not in usedA:
                usedA.add(i)
                ordA.append(i)
                dfsA(k - 1)
                usedA.remove(i)
                ordA.pop()


def dfsT(k):
    global transName, usedT, transT
    if k == 0:
        dfsA(4)
    else:
        for i in transName:
            if i not in usedT:
                usedT.add(i)
                transT.append(i)
                dfsT(k - 1)
                usedT.remove(i)
                transT.pop()


def dfsD(k):
    global usedD, Dord
    if k == 0:
        dfsT(4)
    else:
        for i in range(4):
            if i not in usedD:
                usedD.add(i)
                Dord.append(i)
                dfsD(k - 1)
                Dord.pop()
                usedD.remove(i)


dfsD(4)
