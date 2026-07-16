# leetcode 541
def reverseStr(string: str, k: int) -> str:
    rev = ""

    for i in range(0, len(string), 2 * k):
        win = string[i : i + 2 * k]
        half = win[:k][::-1]
        rev += half + win[k:]
    return rev

print(reverseStr("abcdefg", 2))
