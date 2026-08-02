# Leetcode 2535. Difference Between Element Sum and Digit Sum of an Array
def differenceOfSum(nums):

    element_sum = 0
    digit_sum = 0
    string = ""

    for i in nums:
        element_sum += i
        string += str(i)

    for i in string:
        digit_sum += int(i)
    return element_sum - digit_sum

print(differenceOfSum([1, 15, 6, 3]))
print(differenceOfSum([1, 2, 3, 4, 5]))
