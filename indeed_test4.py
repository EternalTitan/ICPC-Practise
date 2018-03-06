T = int(input().strip())
for t in range(T):
    # ans=[]
    n = int(input().strip())
    data = input().strip()
    counter = [0 for i in range(26)]
    elements = []
    for i in data:
        ch_ord = ord(i) - ord('a')
        temp = (ch_ord + counter[ch_ord]) % 26
        elements.append(chr(temp + ord('a')))
        counter[ch_ord] += 1
    # ans.append(''.join(elements))
    # return ans
    print(''.join(elements))
