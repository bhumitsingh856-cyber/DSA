def sum(arr, target):
    arr.sort()
    pairs = []

    for i in range(len(arr) - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, len(arr) - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue    
            p1 = j + 1
            p2 = len(arr) - 1
            while p1 < p2:
                sum = arr[p1] + arr[p2] + arr[i] + arr[j]
                if sum == target:
                    pairs.append([arr[p1], arr[p2], arr[i], arr[j]])
                    p1 += 1
                    p2 -= 1
                    while p1 < p2 and arr[p1] == arr[p1 - 1]:
                        p1 += 1
                    while p1 < p2 and arr[p2] == arr[p2 + 1]:
                        p2 -= 1
                elif sum < target:
                    p1 += 1
                else:
                    p2 -= 1
    return pairs


print(sum([1, 0, -1, 0, -2, 2], 0))
print(sum([2, 2, 2, 2, 2], 8))
print(sum([-2, -1, -1, 1, 1, 2, 2], 0))
