def closest_sum(arr, target):
    arr.sort()
    diff = float("inf")
    ans = 0
    n = len(arr)
    for i in range(n - 2):
        p1 = i + 1
        p2 = n - 1
        while p1 < p2:
            sum = arr[p1] + arr[p2] + arr[i]
            if sum == target:
                return sum
            elif sum < target:
                p1 += 1
            else:
                p2 -= 1
            if diff > abs(sum - target):
                diff = abs(sum - target)
                ans = sum
    return ans


print(closest_sum([-1, 2, 1, -4], 1))
