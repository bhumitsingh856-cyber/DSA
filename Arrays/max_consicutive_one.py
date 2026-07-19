def max_one(arr):
    count = 0
    mx = 0
    for i in arr:
        if i == 1:
            count += 1
            mx = max(mx, count)
        else:
            count = 0
    return mx


print(max_one([0, 1, 1, 0, 1, 1, 0, 1, 1, 0]))
