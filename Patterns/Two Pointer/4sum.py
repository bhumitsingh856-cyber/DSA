def sum(arr, target):
    arr.sort()
    for i in range(len(arr) - 3):
        for j in range(i + 1, len(arr) - 2):
            p1 = j + 1
            p2 = len(arr) - 1
            while p1 < p2:
                s = arr[p1] + arr[p2] + arr[i] + arr[j]
                if s == target:
                    return [arr[i], arr[j], arr[p1], arr[p2]]
                elif s < target:
                    p1 += 1
                else:
                    p2 -= 1
    return [-1, -1, -1, -1]


print(sum([1, 1, 2, 6, 3, 4, 5, 67, 5, 4, 5], 20))
