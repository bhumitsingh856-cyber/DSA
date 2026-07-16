# leetcode 989
def add(num, k):
    for i in range(len(num) - 1, -1, -1):
        sum = num[i] + k
        num[i] = sum % 10
        k = sum // 10
    while k > 0:
        num.insert(0, k % 10)
        k //= 10
    return num


print(add([1, 2, 0, 0], 9234))
