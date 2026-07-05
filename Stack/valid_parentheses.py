def is_valid(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif i == ")" and stack[-1] == "(":
            stack.pop()
        elif i == "}" and stack[-1] == "{":
            stack.pop()
        elif i == "]" and stack[-1] == "[":
            stack.pop()
        else:
            stack.append(i)
        print(stack)
    return not stack

print(is_valid("(()(){[]})"))
