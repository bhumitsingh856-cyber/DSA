# Leetcode 3798. Largest Even Number


def largestEven(s):
    for i in range(len(s) - 1, -1, -1):
        if int(s[i]) % 2 == 0:
            return s[: i + 1]
    return ""


print(largestEven("1024961"))
print(largestEven("4294967296"))
