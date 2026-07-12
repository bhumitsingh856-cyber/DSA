def reverse(arr):
    p1 = 0
    p2 = len(arr) - 1
    while p1 < p2:
        temp = arr[p1]
        arr[p1] = arr[p2]
        arr[p2] = temp
        p1 += 1
        p2 -= 1
    return arr


print(reverse(["H", "a", "n", "n", "a", "h"]))
