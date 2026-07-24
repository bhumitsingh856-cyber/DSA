def basket(arr):
    low = 0
    basket = 0
    hmap = {}
    for i in range(len(arr)):
        hmap[arr[i]] = hmap.get(arr[i], 0) + 1
        while len(hmap) > 2:
            hmap[arr[low]] -= 1
            if hmap[arr[low]] == 0:
                del hmap[arr[low]]
            low += 1
        basket = max(basket, i - low + 1)
    return basket


print(basket([1, 2, 1]))
print(basket([0, 1, 2, 2]))
print(basket([1, 2, 3, 2, 2]))
