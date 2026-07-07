def remove(arr , target):
    p=0
    for i in range(len(arr)):
        if(arr[i]!=target):
            arr[p] = arr[i]
            p+=1
    return  p,arr[:p]

print(remove([3,2,2,3],3))
    