def helper(width, arr, count, dic, queueSize):
    if width in dic:
        return dic[width], queueSize
    else:
        arr.append(width)
        count.append(0)
        dic[width] = queueSize
        queueSize += 1
        return queueSize - 1, queueSize


T = int(input())
for t0 in range(T):
    n, k = [int(x) for x in input().strip().split()]
    if n == k:
        print('Case #', t0 + 1, ': 0 0', sep='')
        continue
    arr = [n]
    count = [1]
    dic = {}
    tot = 0
    i = 0
    queueSize = 1
    while tot < k:
        flag = False
        if arr[i] & 1:
            temp = arr[i] >> 1
            j, queueSize = helper(temp, arr, count, dic, queueSize)
            count[j] += count[i] * 2
            flag = True
        else:
            temp = (arr[i] - 1) >> 1
            temp += 1
            j, queueSize = helper(temp, arr, count, dic, queueSize)
            count[j] += count[i]
            temp -= 1
            j, queueSize = helper(temp, arr, count, dic, queueSize)
            count[j] += count[i]
            flag = False
        tot += count[i]
        if tot < k:
            i += 1
        else:
            print('Case #', t0 + 1, ': ', sep='', end='')
            if flag:
                print(temp, temp)
            else:
                print(temp + 1, temp)
