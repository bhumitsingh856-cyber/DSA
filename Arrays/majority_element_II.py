# Leetcode 229. Majority Element II


def majorityElement(nums):
    n = len(nums)
    res = []
    hmap = {}
    for i in nums:
        hmap[i] = hmap.get(i, 0) + 1
        if hmap[i] > n / 3:
            res.append(i)
    return res


print(majorityElement([3, 2, 3]))
print(majorityElement([1]))
print(majorityElement([1, 1, 1, 3, 3, 2, 2, 2]) )
