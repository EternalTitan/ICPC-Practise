def is_first_winner(n):
    arr = [False for i in range(113)]
    for i in range(101):
        if not arr[i]:
            arr[i + 2] = True
            arr[i + 3] = True
            arr[i + 5] = True
    if arr[n]:
        return 'First'
    else:
        return 'Second'


t = int(input())
for turns in range(t):
    n = int(input())
