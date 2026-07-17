# leetcode 747
def largest(arr):
    max = 0
    ismax = False
    for i in range(len(arr)):
        if arr[i] > arr[max]:
            max = i
    for i in range(len(arr)):
        if i == max:
            continue
        if arr[max] >= 2 * arr[i]:
            ismax = True
        else:
            ismax = False
            break
    return max if ismax else -1


print(largest([0, 2, 0, 3]))
