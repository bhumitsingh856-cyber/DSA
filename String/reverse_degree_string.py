# Leetcode 3498. Reverse Degree of a String
def reverseDegree(s):
    hmap = {}
    n = 26
    for i in range(65, 91):
        hmap[chr(i).lower()] = n
        n -= 1
    degree = 0
    for i in range(len(s)):
        degree += (i + 1) * hmap[s[i]]
    return degree
