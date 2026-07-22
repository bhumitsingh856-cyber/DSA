# leetcode 1207
def unique(arr):
    hmap = {}
    for i in arr:
        hmap[i] = hmap.get(i, 0) + 1
    s = set()
    for i in hmap:
        s.add(hmap[i])
    return len(s) == len(hmap)


print(unique([1, 2, 2, 1, 1, 3]))
print(unique([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
print(unique([1, 2]))
