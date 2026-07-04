def findMedianSortedArrays( nums1, nums2):
        arr=sorted(nums1+nums2)
        length=len(arr)
        if(length==0):
            return 0
        if(length%2==0):
            return (arr[(length//2)-1]+arr[length//2])/2.0
        else:
            return float(arr[(length)//2])
            
print(findMedianSortedArrays([1,2],[3,4]))
print(findMedianSortedArrays([1,2],[4]))