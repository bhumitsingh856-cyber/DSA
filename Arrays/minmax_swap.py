def minmax_swap(arr):
    if(len(arr)==0):
         return
    min,max=0,0
    for i in range(len(arr)):
        if(arr[min]>arr[i]):
            min=i
        if(arr[max]<arr[i]):
            max=i
    arr[min],arr[max]=arr[max],arr[min]
    return arr
print(minmax_swap([1,2,3,4,5,6,7,8,0]))
              
    
