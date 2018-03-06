import math


def geta(arr):
    ans = []
    for each_data in arr:
        a, b = map(int, each_data.split())
        sqrt_a = math.ceil(math.sqrt(a))
        sqrt_b = math.floor(math.sqrt(b))
        ans.append(sqrt_b - sqrt_a + 1)
    return ans


print(geta(['3 9', '17 24']))
