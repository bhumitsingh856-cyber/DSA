# Leetcode 2798. Number of Employees Who Met the Target
def numberOfEmployeesWhoMetTarget( hours, target):
    count = 0
    for i in hours:
        if i >= target:
            count += 1
    return count

print(numberOfEmployeesWhoMetTarget(hours = [0,1,2,3,4], target = 2))
print(numberOfEmployeesWhoMetTarget(hours = [5,1,2,3,4], target = 2))
