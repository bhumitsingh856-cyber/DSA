# leetcode 1979
def gcd(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    print(min_val, max_val)
    n = 1
    for i in range(2, max_val + 1):
        if min_val % i == 0 and max_val % i == 0:
            n = i
    return n


print(gcd([4, 8]))
