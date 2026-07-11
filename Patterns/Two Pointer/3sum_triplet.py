def sum_pairs(arr):
    arr.sort()
    print(arr)
    pairs = []

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        p1 = i + 1
        p2 = len(arr) - 1
        while p1 < p2:
            if arr[p1] + arr[p2] == -arr[i]:
                pairs.append([arr[i], arr[p1], arr[p2]])
                p1 += 1
                p2 -= 1
                while p1 < p2 and arr[p1] == arr[p1 - 1]:
                    p1 += 1
                while p1 < p2 and arr[p2] == arr[p2 + 1]:
                    p2 -= 1
            elif arr[p1] + arr[p2] < -arr[i]:
                p1 += 1
            else:
                p2 -= 1

    return pairs


print(sum_pairs([-2, 0, 0, 2, 2]))
