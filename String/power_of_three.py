# Leetcode 326. Power of Three

def isPowerOfThree( n):
    a=1
    while a<=n:
        if(a==n):
            return True
        else:
            a=a*3
    return False

print(isPowerOfThree(27))