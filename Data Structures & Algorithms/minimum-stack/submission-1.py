class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        return

    def pop(self) -> None:
        self.stack.pop()
        return
            

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        scd_stack = []
        minimum = self.stack[-1]

        while len(self.stack) > 0:
            minimum = min(minimum, self.stack[-1])
            scd_stack.append(self.stack.pop())
        while len(scd_stack) > 0:
            self.stack.append(scd_stack.pop())
        
        return minimum

        
