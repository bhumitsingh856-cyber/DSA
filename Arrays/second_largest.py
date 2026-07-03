def sec_largest(arr):
    if(len(arr)==0):
        return
    first = second = third = float('-inf')
    for i in arr:
        if i in (first, second, third):
                continue
        if(i>first):
            first,second,third = i,first,second
        elif(i>second):
            second,third = i,second
        elif (i>third):
            third=i 
    return third if third != float('-inf') else first

print(sec_largest([1,2,2,3]))
            
        
        