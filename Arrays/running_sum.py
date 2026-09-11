# Leetcode 1480. Running Sum of 1d Array

def runningSum(nums):
    sm=0
    arr=[]
    for i in range(len(nums)):
        sm+=nums[i]
        arr.append(sm)
    return arr

print(runningSum([1,2,3,4]))