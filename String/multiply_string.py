# Leetcode 43. Multiply Strings

def multiply(num1, num2):
    res = ""
    carry = 0
    for i in range(len(num2) - 1, -1, -1):
        m = (int(num2[i]) * int(num1)) + carry
        carry = m // 10
        res = str(m % 10) + res
    return (str(carry) + res) if carry != 0 else res


print(multiply("2", "3"))
print(multiply("10", "10"))
