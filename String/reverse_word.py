# Leetcode 151. Reverse Words in a String
def reverse(string: str):
    arr = string.strip().split()
    p1 = 0
    p2 = len(arr) - 1
    while p1 < p2:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1
    return " ".join(arr)


print(reverse("151. Reverse Words in a String"))
