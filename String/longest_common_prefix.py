def prefix(arr):
    prefix = ""
    arr.sort()
    for i in range(len(arr[len(arr) - 1])):
        if arr[0][i] != arr[1][i]:
            break
        prefix += arr[0][i]
    return prefix


print(prefix(["dog", "racecar", "car"]))
