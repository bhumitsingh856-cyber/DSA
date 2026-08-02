# Leetcode 67. Add Binary


def addBinary(a, b):
    p1 = len(a) - 1
    p2 = len(b) - 1
    carry = 0
    ans = ""
    while p1 >= 0 or p2 >= 0 or carry:
        n1 = int(a[p1]) if (p1 >= 0) else 0
        n2 = int(b[p2]) if (p2 >= 0) else 0
        sum = n1 + n2 + carry
        carry = sum // 2
        ans = str(sum % 2) + ans
        p1-=1
        p2-=1
    return ans


print(addBinary(a="11", b="1"))
print(addBinary(a="1010", b="1011"))
