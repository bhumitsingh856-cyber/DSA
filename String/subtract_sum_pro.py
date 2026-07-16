# leetcode 1281
def subt(num):
    product = 1
    sum = 0
    for i in str(num):
        product *= int(i)
        sum += int(i)
    return product - sum


print(subt(4421))
