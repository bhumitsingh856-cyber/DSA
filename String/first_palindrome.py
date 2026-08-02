# Leetcode 2108. Find First Palindromic String in the Array
def firstPalindrome(words):
    for i in words:
        isPlaindrome = True
        for j in range(len(i) // 2):
            if i[j] != i[len(i) - 1 - j]:
                isPlaindrome = False
                break
        if isPlaindrome:
            return i
    return ""

print(firstPalindrome(["abc", "car", "ada", "racecar", "cool"]))
print(firstPalindrome(["notapalindrome", "racecar"]))
print(firstPalindrome(["def", "ghi"]))