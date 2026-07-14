def max_value(v1, v2):
    if v1 > v2:
        return v1
    return v2


def sum(arr, k):

    window_sum = 0

    for i in range(k):
        window_sum += arr[i]

    max_sum = window_sum
    low = 1
    high = k

    while high < len(arr):
        window_sum = arr[high] + window_sum - arr[low - 1]
        max_sum = max_value(max_sum, window_sum)
        low += 1
        high += 1
    return max_sum


print(sum([4, 0, 4, 3, 3], 5))
