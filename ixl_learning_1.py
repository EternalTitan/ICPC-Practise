def countHoles(num):
    HOLES = {
        0: 1,
        1: 0,
        2: 0,
        3: 0,
        4: 1,
        5: 0,
        6: 1,
        7: 0,
        8: 2,
        9: 1,
    }
    temp = num
    ret = 0
    while temp > 0:
        digit = temp % 10
        ret += HOLES[digit]
        temp //= 10
    return ret


print(countHoles(630))
