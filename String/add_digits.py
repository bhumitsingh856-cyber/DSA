# Leetcode 258. Add Digits
def add(num):
    while num >= 10:
        sum = 0
        for i in str(num):
            sum += int(i)
        num = sum
    return num


print(add(38))
print(add(0))
