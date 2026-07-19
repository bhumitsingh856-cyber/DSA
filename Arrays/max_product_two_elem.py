# leetcode 1464
def max_prod(arr):

    mx1 = mx2 = float("-inf")

    for i in arr:
        if i > mx1:
            mx2 = mx1
            mx1 = i
        elif i > mx2:
            mx2 = i

    return (mx1 - 1) * (mx2 - 1)

print(max_prod([1, 2]))
