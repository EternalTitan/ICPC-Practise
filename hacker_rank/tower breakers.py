def towerBreakers(n, m):
    if m == 1:
        return 2
    return 2 - (n & 1)
