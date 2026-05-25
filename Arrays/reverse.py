def reverse(arr):
    if(len(arr)==0): return arr
    for i in range (len(arr)//2):
        arr[i] , arr[len(arr)-i-1] =  arr[len(arr)-i-1] , arr[i]
    return arr
print(reverse([1,2,3,4,5]))
print(reverse([5,4,3,2,1]))
print(reverse([]))

