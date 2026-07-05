def two_sum(arr, target):
    if len(arr) == 0:
        return [-1, -1]

    ptr1 = 0
    ptr2 = len(arr) - 1
    while ptr1 < ptr2:
        if arr[ptr1] + arr[ptr2] == target:
            return [ptr1, ptr2]
        if arr[ptr1] + arr[ptr2] < target:
            ptr1 += 1
        else:
            ptr2 -= 1
    return [-1, -1]


print(two_sum([1, 2, 3, 4, -5], -3))
