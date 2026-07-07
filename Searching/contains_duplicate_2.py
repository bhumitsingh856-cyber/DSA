def contains(arr):
    d={}
    for i in range(len(arr)):
        d[i]=arr[i]
    
    for i in d:
        print(d[i])

contains([1,2,3,1])