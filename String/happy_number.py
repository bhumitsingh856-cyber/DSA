# Leetcode 202. Happy Number
def happy(n):
    visited = set()
    while n != 1 and (n not in visited):
        visited.add(n)
        new = 0
        for i in str(n):
            new += int(i) ** 2
        n = new
    return n == 1


print(happy(19))
print(happy(2))
