# Leetcode 268. Missing Number

def missingNumber(nums):
    total = sum([i for i in range(1,len(nums)+1)])
    arr_sum = sum(nums)
    return total-arr_sum 

def missingNumber2(nums):
    n=set(nums)
    for i in range(len(nums)): 
        if(i not in n):
            return i



print(missingNumber([3,0,1]))
print(missingNumber2([3,0,1]))
print(missingNumber([9,6,4,2,3,5,7,0,1]))
print(missingNumber2([9,6,4,2,3,5,7,0,1]))