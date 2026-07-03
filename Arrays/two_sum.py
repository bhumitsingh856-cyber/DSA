# Sorted array
def two_sum(arr , target):
    p1=0
    p2=len(arr)-1
    while p1<p2:
        if(arr[p1]+arr[p2] == target):
            return [p1,p2]
        if(arr[p1]+arr[p2]<target):
            p1+=1
        if(arr[p1]+arr[p2]>target):
            p2-=1
    return [-1,-1]

print(two_sum([2,7,11,15],9))
        
    