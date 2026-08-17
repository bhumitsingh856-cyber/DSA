# Leetcode 53. Maximum Subarray


def maxSubArray(nums):
    max_sum = nums[0]
    ans = nums[0]
    for i in range(1, len(nums)):
        v1 = nums[i] + max_sum
        v2 = nums[i]
        max_sum = max(v1, v2)
        ans = max(ans, max_sum)
    return ans


print(maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray(nums=[5, 4, -1, 7, 8]))
