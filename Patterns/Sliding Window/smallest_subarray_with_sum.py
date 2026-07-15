# LC 209
def smallest_subarray(arr, k):
    n = len(arr)
    low = 0
    high = 0
    min_len = float("inf")
    sum = 0
    while high < n:
        sum += arr[high]
        while sum >= k:
            l = high - low + 1
            min_len = min(min_len, l)
            sum -= arr[low]
            low += 1
        high += 1
    return min_len if min_len != float("inf") else 0


print(smallest_subarray([2, 3, 1, 2, 4, 3], 7))
