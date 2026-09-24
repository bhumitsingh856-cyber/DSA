# Leetcode 3550. Smallest Index With Digit Sum Equal to Index

def smallestIndex(nums):
    for i in range(len(nums)):
        digit_sum = 0
        num = nums[i]
        for j in str(num):
            digit_sum+=int(j)
        if(i == digit_sum):
            return i
    return -1

print(smallestIndex([1,3,2]))