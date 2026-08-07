# Leetcode 3345. Smallest Divisible Digit Product I
def product(s):
    prod = 1
    for i in s:
        prod *= int(i)
    return prod

def smallest(n, t):
    prod = product(str(n))
    if prod % t == 0:
        return n
    for i in range(n, n + t):
        res = product(str( i))
        if res % t == 0:
            return i
    return -1

print(smallest(n=10, t=2))
