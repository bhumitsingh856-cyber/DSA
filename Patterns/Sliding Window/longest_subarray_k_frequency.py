# Leetcode 2958. Length of Longest Subarray With at Most K Frequency


def maxSubarrayLength(nums, k):
    hmap = {}
    max_len = 0
    left = 0
    for right in range(len(nums)):
        n = nums[right]
        hmap[n] = hmap.get(n, 0) + 1
        while hmap[n] > k:
            hmap[nums[left]] -= 1
            if hmap[nums[left]] <= 0:
                del hmap[nums[left]]
            left += 1
        max_len = max(right - left + 1, max_len)
    return max_len


print(maxSubarrayLength(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2))
print(maxSubarrayLength(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1))
print(maxSubarrayLength(nums=[5, 5, 5, 5, 5, 5, 5], k=4))
print(maxSubarrayLength(nums=[1, 4, 4, 3], k=1))
print(maxSubarrayLength(nums=[1], k=1))
