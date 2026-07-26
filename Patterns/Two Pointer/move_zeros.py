# Leetcode 283. Move Zeroes


def move_zero(arr):
    p1 = 0
    p2 = 0
    while p2 < len(arr):
        if arr[p2] != 0:
            arr[p2], arr[p1] = arr[p1], arr[p2]
            p1 += 1
        p2 += 1
    return arr


def move_zero2(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr.append(arr.pop(i))
    return arr


print(move_zero([0, 1, 0, 3, 12]))
print(move_zero([1, 2, 3, 4]))
print(move_zero2([0, 1, 0, 3, 12]))
print(move_zero2([1, 2, 3, 4]))
