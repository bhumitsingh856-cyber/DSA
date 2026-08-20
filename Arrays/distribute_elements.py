# Leetcode 3069. Distribute Elements Into Two Arrays I
def resultArray( nums):
    arr1=[nums[0]]
    arr2=[]
    for i in range(1,len(nums)):
        if(not arr2):
            arr2.append(nums[i])
        else:
            if(arr1[-1] > arr2[-1]):
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
    return arr1+arr2