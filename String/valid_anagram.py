def anagram(s1, s2):
    hmap = {}
    if not len(s1) == len(s2):
        return False
    for i in s1:
        hmap[i] = hmap.get(i, 0) + 1
    for i in s2:
        hmap[i] = hmap.get(i, 0) - 1
        if hmap[i] <= 0:
            del hmap[i]
    return not hmap


print(anagram(s1="anagram", s2="nagaram"))
