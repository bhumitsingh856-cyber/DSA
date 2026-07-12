def remove(arr):
    p1 = 2
    for i in range(2, len(arr)):
        if arr[i] != arr[p1 - 2]:
            arr[p1] = arr[i]
            p1 += 1
    return p1

print(remove([1,1,1,2,2,3]))
