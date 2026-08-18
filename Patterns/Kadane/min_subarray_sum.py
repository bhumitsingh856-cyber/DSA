# 
def minSubarraySum(arr):
    min_sum=arr[0]
    ans=arr[0]
    for i in range(1,len(arr)):
        v1 = min_sum+arr[i]
        min_sum=min(v1,arr[i])
        ans=min(ans,min_sum)
    return ans

print(minSubarraySum([3,-4, 2,-3,-1, 7,-5]))
print(minSubarraySum( [2, 6, 8, 1, 4]))