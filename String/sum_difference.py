# Leetcode 2894. Divisible and Non-divisible Sums Difference

def differenceOfSums(n, m):
    n1_sum = 0
    n2_sum = 0
    for i in range(1, 1 + n):
        if i % m != 0:
            n1_sum += i
    for i in range(1, 1 + n):
        if i % m == 0:
            n2_sum += i
    return n1_sum - n2_sum

print(differenceOfSums(10, 3))