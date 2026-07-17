def double_exist(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i != j and arr[i] == 2 * arr[j]:
                return True
    return False


print(double_exist([3, 1, 7, 11]))
