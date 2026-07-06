 
def sortedSquares(nums):
        neg=[]
        pos=[]
        for i in nums:
            if(i<0):
                neg.append(i)
            else:
                pos.append(i)
        neg=[i*i for i in neg]
        pos=[i*i for i in pos]
        print(neg,pos)
        if(not neg):
            return pos
        if(not pos):
            neg.reverse()
            return neg

        p1=0
        p2=0
        result=[]
        neg.reverse()
        while(p1<len(neg) and p2<len(pos)):
            if(neg[p1] < pos[p2]):
                result.append(neg[p1])
                p1+=1
            else:
                result.append(pos[p2])
                p2+=1
        while(p1<len(neg)):
            result.append(neg[p1])
            p1+=1
        while(p2<len(pos)):
            result.append(pos[p2])
            p2+=1
        return result

print(sortedSquares([-1,-1]))