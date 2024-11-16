from functools import cache

def solve1():
    n = 4097905
    k = 1

    while k * k < n:
        k += 1
    x = k * 2 - 1
    missing = k*k - n
    return missing * x

@cache
def thickness(layer, priests, M):
    if layer == 1:
        return 1

    return (thickness(layer-1, priests, M) * priests) % M

def solve2(blocks, priests, M):
    k = 1
    total = 0
    while total < blocks:
        total += thickness(k, priests, M) * (k * 2 - 1)
        k += 1
    k = ((k-1) * 2) - 1
    return (total-blocks) * k

print(solve1())
print(solve2(20240000, 446, 1111))
