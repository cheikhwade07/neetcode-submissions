class MinStack:

    def __init__(self):
        self.stack= []
        self.min_stack=[float('inf')]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_stack[-1] :
            self.min_stack.append(val)
    def pop(self) -> None:
        removed = self.stack.pop()
        if removed == self.min_stack[-1]:
            self.min_stack.pop()

        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.stack:
            return self.min_stack[-1]
