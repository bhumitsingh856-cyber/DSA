# Leetcode 415 Add Strings
def add_string(num1, num2):
    p1 = len(num1) - 1
    p2 = len(num2) - 1
    result = ""
    carry = 0
    while p1 >= 0 and p2 >= 0:
        a = int(num1[p1])
        b = int(num2[p2])
        sm = a + b + carry
        if sm <= 9:
            result = str(sm) + result
            carry = 0
        else:
            carry = sm // 10
            result = str(sm % 10) + result
        p1 -= 1
        p2 -= 1
    while p1 >= 0:
        sm = int(num1[p1]) + carry
        if sm <= 9:
            result = str(sm) + result
            carry = 0
        else:
            carry = sm // 10
            result = str(sm % 10) + result
        p1 -= 1
    while p2 >= 0:
        sm = int(num2[p2]) + carry
        if sm <= 9:
            result = str(sm) + result
            carry = 0
        else:
            carry = sm // 10
            result = str(sm % 10) + result
        p2 -= 1
    if carry != 0:
        result = str(carry) + result
    return result


# Optimized Code
def add_string_optimized(num1, num2):
    p1, p2 = len(num1) - 1, len(num2) - 1
    carry = 0
    result = []

    while p1 >= 0 or p2 >= 0 or carry:
        digit1 = int(num1[p1]) if p1 >= 0 else 0
        digit2 = int(num2[p2]) if p2 >= 0 else 0

        total = digit1 + digit2 + carry
        carry = total // 10
        result.append(str(total % 10))

        p1 -= 1
        p2 -= 1

    return "".join(reversed(result))


print(add_string("6994", "36"))
print(add_string_optimized("6994", "36"))
print(add_string("99", "9999"))
print(add_string_optimized("99", "9999"))
