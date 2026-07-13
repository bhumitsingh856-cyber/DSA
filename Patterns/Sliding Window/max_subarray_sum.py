def max_value(v1, v2):
    if v1 > v2:
        return v1
    return v2
    
def sum(arr, k):
    max_sum = 0
    window_sum = 0
    for i in range(k):
        window_sum += arr[i]
    low = 1
    high = k
    while high < len(arr):
        window_sum = arr[high] + window_sum - arr[low - 1]
        max_sum = max_value(max_sum, window_sum)
        low += 1
        high += 1
    return max_sum


print(sum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
