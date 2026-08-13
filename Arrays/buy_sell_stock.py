# Leetcode 121. Best Time to Buy and Sell Stock

def maxProfit(arr):
    min_price = float("inf")
    max_profit = 0
    for i in arr:
        min_price = min(i, min_price)
        if i > min_price:
            profit = i - min_price
            max_profit = max(max_profit, profit)
    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
