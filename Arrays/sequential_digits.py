# Leetcode 1291. Sequential Digits


def sequentialDigits(low, high):
    ans = []
    s = "123456789"
    for i in range(9):
        for j in range(i + 1, 10):
            res = s[i:j]
            if low <= int(res) <= high:
                ans.append(int(res))
    return sorted(ans)


print(sequentialDigits(100, 1300))
