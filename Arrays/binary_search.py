def binarySearch(arr,target):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(end+start)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]<target):
            start=mid+1
        else:
            end=mid-1
    return -1

print(binarySearch([1,2,3,4,5],3))        
