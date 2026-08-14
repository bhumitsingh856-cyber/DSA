# Leecode 3090. Maximum Length Substring With Two Occurrences


def maximumLengthSubstring(s):
    hmap = {}
    low = 0
    max_len = 0
    for high in range(len(s)):
        char = s[high]
        hmap[char] = hmap.get(char, 0) + 1
        while hmap[char] > 2:
            hmap[s[low]] -= 1
            if hmap[s[low]] <= 0:
                del hmap[s[low]]
            low += 1
        max_len = max(max_len, high - low + 1)
    return max_len


print(maximumLengthSubstring("aabcbcdbca"))
print(maximumLengthSubstring("aaabbbcccc"))
