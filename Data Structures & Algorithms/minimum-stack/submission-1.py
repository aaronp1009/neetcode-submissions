class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # Store a tuple (val, currentMin)
        if not self.stack:
            self.stack.append((val, val))
        else:
            # Check the previous to see if that min is less
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        # We know it only gets called on non-empty stacks
        return self.stack[-1][1]