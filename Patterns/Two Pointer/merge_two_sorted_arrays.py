def merge(arr1, arr2):
    if not arr1:
        return arr2
    if not arr2:
        return arr1
    p1, p2 = 0, 0
    result = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            result.append(arr1[p1])
            p1 += 1
        else:
            result.append(arr2[p2])
            p2 += 1
    while p1 < len(arr1):
        result.append(arr1[p1])
        p1 += 1
    while p2 < len(arr2):
        result.append(arr2[p2])
        p2 += 1

    return result


print(merge([1, 2, 3], [0,1, 5, 7,8]))
