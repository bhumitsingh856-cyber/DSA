#  Leetcode 594. Longest Harmonious Subsequence
def harmonius(arr):
    arr.sort()
    p1 = 0
    p2 = 0
    max_len = 0
    while p2 < len(arr):
        diff = arr[p2] - arr[p1]
        if diff == 1:
            max_len = max(p2 - p1 + 1, max_len)
        if diff > 1:
            p1 += 1
        
        p2 += 1
    return max_len


print(harmonius([1, 3, 2, 2, 5, 2, 3, 7]))
print(harmonius([1, 2, 3, 4]))
print(harmonius([1, 1, 1]))
