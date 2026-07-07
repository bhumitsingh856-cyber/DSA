def duplicate(arr):
    d:dict={}
    for i in arr:
        if(not d.get(i)):
            d[i]=1
        else:
            d[i]+=1
    for i in d:
        if(d.get(i)>1):
            return True
    return False
print(duplicate([1,2,3,4,5,5,2]))
print(duplicate([1,2,3,4,5]))