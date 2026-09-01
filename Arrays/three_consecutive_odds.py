# Leetcode 1550. Three Consecutive Odds


def threeConsecutiveOdds(arr):
    count = 0
    for i in arr:
        if i % 2 != 0:
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False


print(threeConsecutiveOdds(arr=[2, 6, 4, 1]))
print(threeConsecutiveOdds(arr=[1, 2, 3, 4, 5, 6, 7]))