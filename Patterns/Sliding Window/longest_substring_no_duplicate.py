# Leetcode 3. Longest Substring Without Repeating Characters
def subarray(string):
    p1 = 0
    hset = set()
    longest = 0
    for i in range(len(string)):
        while string[i] in hset:
            hset.remove(string[p1])
            p1 += 1
        hset.add(string[i])
        longest = max(longest, i - p1 + 1)
    return longest

print(subarray("abcabcbb"))
print(subarray("bbbbb"))
print(subarray("pwwkew"))
