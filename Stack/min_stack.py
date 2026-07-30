class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, value):
        self.stack.append(value)
        if len(self.min) == 0 or value <= self.min[-1]:
            self.min.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return
        val = self.stack.pop()
        if val == self.min[-1]:
            self.min.pop()

    def top(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def getMin(self):
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
print(obj.stack, obj.min)
obj.push(0)
print(obj.stack, obj.min)
obj.push(-3)
print(obj.stack, obj.min)
obj.pop()
print(obj.stack, obj.min)
print(obj.top())
print(obj.getMin())
