def unique(arr):
    a={}
    for i in arr:
        if(i not in a):
            a[i]=1
        else:
            a[i]=a[i]+1
    for i in a :
        if(a[i]==1):
            print(i)
(unique([1,2,2]))
