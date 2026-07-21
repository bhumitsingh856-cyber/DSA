# leetcode 682
def game(arr):
    stack = []
    for i in arr:
        if i == "C":
            stack.pop()
        elif i == "D":
            stack.append(stack[-1] * 2)
        elif i == "+":
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(i))
    return sum(stack)


print(game(["5", "2", "C", "D", "+"]))
print(game(["1", "C"]))
print(game(["5", "-2", "4", "C", "D", "9", "+", "+"]))
