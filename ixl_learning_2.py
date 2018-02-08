def getMinimumDifference(a, b):
    ALPHABET_SIZE = 26
    n = len(a)
    ret = []
    for case in range(n):
        if len(a[case]) != len(b[case]):
            ret.append(-1)
            continue
        counter_a = [0 for i in range(ALPHABET_SIZE)]
        counter_b = [0 for i in range(ALPHABET_SIZE)]
        difference = [0 for i in range(ALPHABET_SIZE)]
        for each_char in a[case]:
            counter_a[ord(each_char) - ord('a')] += 1

        for each_char in b[case]:
            counter_b[ord(each_char) - ord('a')] += 1

        for i in range(ALPHABET_SIZE):
            difference[i] = counter_a[i] - counter_b[i]

        tot = 0
        for i in range(ALPHABET_SIZE):
            if difference[i] > 0:
                tot += difference[i]
        ret.append(tot)
    return ret


print(getMinimumDifference(['a', 'jk', 'abb', 'mn', 'abc'], ['bb', 'kj', 'bbc', 'op', 'def']))
