out = open("2.out", "w")
T = int(input())
for t0 in range(T):
    out.write("Case #" + str(t0 + 1) + ": ")
    n, r, o, y, g, b, v = [int(x) for x in input().strip().split()]
    if o > b or g > r or v > y:
        out.write("IMPOSSIBLE\n")
    else:
        if (o > 0 and o == b and n - o > o) or (g > 0 and g == r and n - g > g) or (v > 0 and v == y and n - v > v):
            out.write("IMPOSSIBLE\n")
        else:
            tyy = yy = y - v - 1
            tbb = bb = b - o - 1
            trr = rr = r - g - 1
            if yy > bb + rr + 1 or bb > yy + rr + 1 or rr > bb + yy + 1:
                out.write("IMPOSSIBLE\n")
            else:
                color = [[yy, 'Y'], [bb, 'B'], [rr, 'R']]
                color.sort(key=lambda x: x[0], reverse=True)
                ins = []
                loc = 0
                while color[0][0] > 0:
                    color[0][0] -= 1
                    ins.append(color[0][1])
                    if color[1][0] >= color[2][0] and color[1][0] > 0:
                        color[1][0] -= 1
                        ins.append(color[1][1])
                    elif color[2][0] > 0:
                        color[2][0] -= 1
                        ins.append(color[2][1])
                while color[1][0] + color[2][0] > 0:
                    if ins[-1] == color[1][1]:
                        ins.append(color[2][1])
                        color[2][0] -= 1
                    else:
                        ins.append(color[1][1])
                        color[1][0] -= 1
                if len(ins) > 0:
                    if ins[0] != 'B' and ins[-1] != 'R':
                        loc = 1
                    elif ins[0] != 'R' and ins[-1] != 'Y':
                        loc = 2
                    elif ins[0] != 'Y' and ins[-1] != 'B':
                        loc = 3
                for i in range(o):
                    out.write("BO")
                if b > o:
                    out.write("B")
                if loc == 1:
                    out.write("".join(ins))
                for i in range(g):
                    out.write("RG")
                if r > g:
                    out.write("R")
                if loc == 2:
                    out.write("".join(ins))
                for i in range(v):
                    out.write("YV")
                if y > v:
                    out.write("Y")
                if loc == 3:
                    out.write("".join(ins))
                out.write("\n")
