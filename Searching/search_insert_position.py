# # O(n)
# def position(arr,target):
#     if(arr[len(arr)-1]<=target):
#         return len(arr)
#     p=0
#     while p<=len(arr):
#         if(arr[p]>=target):
#             return p
#         p+=1
#     return -1

# print(position([1,3,5,6],0))
def position(arr,target):
    if(arr[len(arr)-1]<=target):
        return len(arr)
    p1=0
    p2=len(arr)-1
    while p1<=p2:
        mid=(p1+p2) // 2
        if(arr[mid] == target):
            return mid
        elif(arr[mid]<target):
            p1=mid+1
        else:
            p2=mid-1
    return p1
print(position([1,3,5,6],4))

