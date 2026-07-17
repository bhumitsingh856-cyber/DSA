def reverse(string):
    arr = list(string)
    p1 = 0
    p2 = len(arr) - 1
    vowels = set(["a", "e", "i", "o", "u"])
    while p1 < p2:
        if arr[p1].lower() in vowels and arr[p2].lower() in vowels:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p1 += 1
            p2 -= 1
        elif not arr[p1].lower() in vowels:
            p1 += 1
        else:
            p2 -= 1

    return "".join(arr)


print(reverse("leetcode"))
print(reverse("icecream"))
