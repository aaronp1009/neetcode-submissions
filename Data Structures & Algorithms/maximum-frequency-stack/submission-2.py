class FreqStack:

    def __init__(self):
        self.count = {} # Keep track of our frequencies for each int
        self.stacks = [[]] # Stack of stacks, each stack is the frequency, first is just a placeholder
        
    def push(self, val: int) -> None:
        valCount = 1 + self.count.get(val, 0) # Get the current count from hashmap, add 1 to it
        self.count[val] = valCount # Update the hashmap's frequency
        if valCount == len(self.stacks): # We need a new stack for this before appending
            self.stacks.append([])
        # Add to the correct stack, we made sure it will exist
        self.stacks[valCount].append(val)

    def pop(self) -> int:
        # The top of the last stack is what we want to pop.
        poppedVal = self.stacks[-1].pop()

        # We must reduce the count and check if this stack should be removed to avoid pop errors.
        self.count[poppedVal] -= 1

        if not self.stacks[-1]:
            self.stacks.pop()

        return poppedVal
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()