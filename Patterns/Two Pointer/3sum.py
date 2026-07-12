# Target - 0
def sum(arr):
    arr.sort()
    if not arr:
        return [-1, -1, -1]
    p1 = 1
    p2 = len(arr) - 1
    for i in range(len(arr)):
        while p1 < p2:
            if arr[p1] + arr[p2] == -arr[i]:
                return [i, p1, p2]
            elif arr[p1] + arr[p2] < arr[i]:
                p1 += 1
            else:
                p2 -= 1
    return [-1, -1, -1]


print(sum([-1, -2, -3, 4, 5, 6]))

# Target


def target_sum(arr, target):
    arr.sort()
    if not arr:
        return [-1, -1, -1]
    p1 = 1
    p2 = len(arr) - 1
    for i in range(len(arr)):
        while p1 < p2:
            if arr[p1] + arr[p2] + arr[i] == target:
                return [i, p1, p2], [arr[i], arr[p1], arr[p2]]
            elif arr[p1] + arr[p2] + arr[i] < target:
                p1 += 1
            else:
                p2 -= 1
    return [-1, -1, -1]


print(target_sum([1, 2, 3, 4, 5, 6], 10))
