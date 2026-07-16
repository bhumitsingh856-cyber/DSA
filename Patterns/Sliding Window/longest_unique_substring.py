def substring(string, k):
    n = len(string)
    low = 0
    max_len = 0
    hmap = {}
    for i in range(n):
        char = string[i]
        if not hmap.get(char):
            hmap[char] = 1
        else:
            hmap[char] += 1
        while len(hmap) > k:
            hmap[string[low]] -= 1
            if hmap[string[low]] == 0:
                del hmap[string[low]]
            low += 1

        max_len = max(max_len, i - low + 1)
    return max_len


print(substring("eceba", 2))
