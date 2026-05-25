def linearSearch(arr,target):
    for i in range(len(arr)):
        if(arr[i]==target):
            return i 
    return -1
print(linearSearch([1,2,3,4,5],2))