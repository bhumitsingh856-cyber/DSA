def reverse(a):
    string=list(str(abs(a)))
    # if(a<0):
    #         string=list(str(a*-1))
    # else:
    #         string=list(str(a))
    for i in range(len(string)//2):
        temp=string[i]
        string[i] = string[len(string)-i-1] 
        string[len(string)-i-1] = temp
    rev=int(''.join(string))
    result=rev*-1 if a<0 else rev
    if(result<-2**31 or result>2**31):
        return 0
    return  result
print(reverse(-120))