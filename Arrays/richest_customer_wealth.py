# Leetcode 1672. Richest Customer Wealth

def maximumWealth(accounts):
    mx=float('-inf')
    for i in accounts:
        c_sum = sum(i)
        mx=max(c_sum,mx)
    return mx

print(maximumWealth(accounts = [[1,2,3],[3,2,1]]))
print(maximumWealth(accounts = [[2,8,7],[7,1,3],[1,9,5]]))