def max_average(arr, k):
    n = len(arr)
    if n == 1:
        return arr

    max_sum = 0
    for i in range(k):
        max_sum += arr[i]
    left = 0
    right = k
    current_sum = max_sum
    while right < n:
        current_sum = arr[right] + current_sum - arr[left - 1]
        max_sum = max(max_sum, current_sum)
        left += 1
        right += 1

    return max_sum / k


print(max_average([4, 0, 4, 3, 3], 4))
