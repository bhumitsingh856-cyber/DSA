# Leetcode 3718. Smallest Missing Multiple of K

def missingMultiple(nums, k):
    i = k
    while i:
        if i not in nums:
            return i
        i += k

print(missingMultiple(nums=[1, 3, 6, 10], k=2))
print(missingMultiple(nums=[3, 6, 9, 12], k=3))
