def occurance(arr,target):
    if(not arr):
        return [-1,-1]
    p1=0
    p2=len(arr)-1
    occ=[-1,-1]
    while(p1<=p2):
        if(occ[0]==-1 ):
            if (arr[p1]==target):
                occ[0]=p1
            else:
                p1+=1
        if(occ[1]==-1 ):
            if(arr[p2]==target):
                occ[1]=p2
            else:
                p2-=1
        if(occ[0] != -1 and occ[1]!=-1):
            return occ
        
    return occ

print(occurance([5,7,7,8,10],8))
        
        