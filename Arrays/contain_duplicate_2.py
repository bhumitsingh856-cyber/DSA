# 219. Contains Duplicate II
def duplicate(arr, k):
    hmap = {}
    for i in range(len(arr)):
        if arr[i] in hmap:
            if abs(hmap[arr[i]] - i) <= k:
                return True
        hmap[arr[i]] = i
    return False


print(duplicate([1, 2, 3, 1], 3))
print(duplicate([1, 2, 3, 1, 2, 3], k=2))
print(duplicate([1, 0, 1, 1], k=1))
