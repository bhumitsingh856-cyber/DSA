# leetcode 488
def numbers(array):
    arr = set(array)
    diss = []
    for i in range(1, len(array) + 1):
        if i not in arr:
            diss.append(i)
    return diss


print(numbers([1, 1]))
