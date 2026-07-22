# Leet code 387
def firstUniqChar(s):
    hmap = {}
    for i in s:
        hmap[i] = hmap.get(i, 0) + 1
    for i in range(len(s)):
        if hmap[s[i]] == 1:
            return i
    return -1 

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))
