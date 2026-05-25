def intersect(arr1,arr2):
    for i in arr1:
        if(i in arr2):
            print(i)    
print(intersect([1,2,3,1,4,5,1],[1,1,3,4,5,6,7]))