# Leetcode 152. Maximum Product Subarray
def maxProduct(nums):
    prod=nums[0]
    max_prod=nums[0]
    for i in range(1,len(nums)):
        p1=prod * nums[i]
        p2=nums[i]
        prod=max(p1,p2)
        max_prod=max(max_prod,prod)
    return max_prod

print(maxProduct(nums = [2,3,-2,4]))
print(maxProduct(nums = [-2,0,-1]))