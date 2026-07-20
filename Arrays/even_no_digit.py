# Leetcode 1295 
def even(arr):
    count = 0
    i = 0
    j = len(arr) - 1
    while i <= j:
        if i == j:
            if len(str(arr[i])) % 2 == 0:
                count += 1
        else:
            if len(str(arr[i])) % 2 == 0:
                count += 1
            if len(str(arr[j])) % 2 == 0:
                count += 1
        j -= 1
        i += 1
    return count


print(even([12, 345, 2, 6, 7896]))
