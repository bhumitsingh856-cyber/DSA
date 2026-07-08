def sum(arr,target):
    print(arr)
    p1=0
    p2=len(arr)-1
    pairs=[]
    while p1<p2:
        sum=arr[p1]+arr[p2]
        if  sum == ta*rget:
            pairs.append((p1,p2))
            p1+=1
            p2-=1
        elif(sum<target):
            p1+=1
        else:
            p2-=1
        while(arr[p1] == arr[p1-1]):
            p1+=1
        while(arr[p2] == arr[p2-1]):
            p2-=1
    return pairs

print(sum([1,1,2,2,3,3,4],6))