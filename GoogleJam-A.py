T = int(input())
for t0 in range(T):
    st, k = input().strip().split()
    k = int(k)
    st = list(map((lambda x: True if x == '+' else False), list(st)))
    lenSt = len(st)
    queue = []
    queueSize = 0
    ans = 0
    flip = False
    for i in range(lenSt - k + 1):
        if queueSize > 0:
            if queue[0] == i:
                flip = not flip
                queue.pop(0)
                queueSize -= 1
        if not flip ^ st[i]:
            ans += 1
            flip = not flip
            queue.append(i + k)
            queueSize += 1
    for i in range(lenSt - k + 1, lenSt):
        if queueSize > 0:
            if queue[0] == i:
                flip = not flip
                queue.pop(0)
                queueSize -= 1
        if not flip ^ st[i]:
            ans = 'IMPOSSIBLE'
            break
    print('Case #', t0 + 1, ': ', ans, sep='')
