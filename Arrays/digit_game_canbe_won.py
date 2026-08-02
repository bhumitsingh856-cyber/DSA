# Leetcode 3232. Find if Digit Game Can Be Won
def canAliceWin(nums):
    single = 0
    double = 0
    for i in nums:
        if i < 10:
            single += i
        else:
            double += i
    return single > double or single < double


print(canAliceWin([1, 5, 12, 20]))
print(canAliceWin([11, 10, 5, 20]))
print(canAliceWin([1, 2, 3, 4, 10]))
