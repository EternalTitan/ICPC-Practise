def count_palindromes(S):
    def get_partial_sum(a, b):
        if a == 0:
            return partial_sum_forward[b]
        else:
            return partial_sum_forward[b] - partial_sum_forward[a - 1]

    partial_sum_forward = [ord(S[0])]
    len_s = len(S)
    for i in range(1, len_s):
        partial_sum_forward.append(partial_sum_forward[i - 1] + ord(S[i]))
    counter = 0
    for i in range(len_s):
        for j in range(i, len_s):
            if i == j:
                counter += 1
            else:
                half_size = (j - i + 1) // 2
                if get_partial_sum(i, i + half_size - 1) == get_partial_sum(j - half_size + 1, j):
                    is_palindromes = True
                    for k in range(half_size):
                        if S[i + k] != S[j - k]:
                            is_palindromes = False
                            break
                    if is_palindromes:
                        # for k in range(i,j+1):
                        # print(S[k],sep='',end='')
                        # print()
                        counter += 1
    return counter

# print(count_palindromes("hellolle"))
