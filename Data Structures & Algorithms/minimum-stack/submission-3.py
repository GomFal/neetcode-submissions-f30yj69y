class MinStack:
    def __init__(self):
        self.minStack = [] # Stack with pair values: (value, minValue) -> minValue is the minimum Value of the stack

    def push(self, val: int) -> None:
        if not self.minStack or self.minStack[-1][1] > val:
            self.minStack.append((val, val))
        else:
            self.minStack.append((val, self.minStack[-1][1]))
        
    def pop(self) -> None:
        self.minStack.pop()
        
    def top(self) -> int:
        return self.minStack[-1][0]
        
    def getMin(self) -> int:
        return self.minStack[-1][1]