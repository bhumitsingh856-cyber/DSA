def duplicate(arr):
    unique = 1
    p1 = 0
    p2 = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            p2 += 1
        else:
            p1 += 1
            arr[p1] = arr[i]
            p2 += 1
            unique += 1
    print(arr)
    return unique


print(duplicate([1, 1, 2, 2, 3, 3, 4]))
