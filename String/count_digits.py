# Leetcode 2520. Count the Digits That Divide a Number
def countDigits(num):
    count = 0
    for i in str(num):
        if int(i) != 0 and num % int(i) == 0:
            count += 1
    return count

print(countDigits(7))
print(countDigits(128))
print(countDigits(1012))
