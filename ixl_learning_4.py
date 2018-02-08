import math


def reducedFractionSums(expressions):
    ret = []
    for each_expression in expressions:
        temp = each_expression.split('+')
        a, b = map(int, temp[0].split('/'))
        c, d = map(int, temp[1].split('/'))
        e = a * d + b * c
        f = b * d
        gcd = math.gcd(e, f)
        temp = str(e // gcd) + '/' + str(f // gcd)
        ret.append(temp)
    return ret


reducedFractionSums(['722/148+360/176'])
