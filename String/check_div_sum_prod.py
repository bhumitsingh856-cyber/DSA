# Leetcode 3622. Check Divisibility by Digit Sum and Product

def checkDivisibility(n):
    prod=1
    sm=0
    for i in str(n):
        sm+=int(i)
        prod*=int(i)
    return n%(prod+sm)==0

print(checkDivisibility(12))
print(checkDivisibility(99))
print(checkDivisibility(2))