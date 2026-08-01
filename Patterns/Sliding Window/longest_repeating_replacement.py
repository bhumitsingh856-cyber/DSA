# Leetcode 424. Longest Repeating Character Replacement
def substring(s, k):
    hmap = {}
    p1 = 0
    max_count = 0
    max_len = 0
    for i in range(len(s)):
        hmap[s[i]] = hmap.get(s[i], 0) + 1
        max_count = max(max_count, hmap[s[i]])
        diff = (i - p1 + 1) - max_count

        if diff > k:
            hmap[s[p1]] -= 1
            p1 += 1
        max_len = max(max_len, i - p1 + 1)
    return max_len


print(substring(s="ABAB", k=2))
print(substring(s="AABABBA", k=1))
