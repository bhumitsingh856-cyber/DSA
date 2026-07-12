def sort_colors(arr):

    p1 = 0
    p2 = len(arr) - 1
    i = 0
    while i <= p2:
        if arr[i] == 0:
            arr[i], arr[p1] = arr[p1], arr[i]
            p1 += 1
        elif arr[i] == 2:
            arr[i], arr[p2] = arr[p2], arr[i]
            p2 -= 1
        else:
            i += 1
    return arr


print(sort_colors([1, 1, 0, 0, 2, 2, 1, 1]))
print(sort_colors([1, 2, 0]))
print(sort_colors([2, 0, 2, 1, 1, 0]))
