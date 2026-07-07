def merge(arr1,arr2,m,n):
    # if(n==0):
    #     return arr1
    p1=m-1
    p2=n-1
    w=(m+n)-1
    while  p1>=0 and p2>=0:
        if(arr1[p1]<arr2[p2]):
            arr1[w] = arr2[p2]
            p2-=1

        else:
            arr1[w] = arr1[p1]
            p1-=1
        
        w-=1
        
    while p2 >= 0:
        arr1[w] = arr2[p2]
        p2 -= 1
        w -= 1
    
    return arr1
print(merge([1,2,3,0,0,0],[2,5,6],3,3))
    