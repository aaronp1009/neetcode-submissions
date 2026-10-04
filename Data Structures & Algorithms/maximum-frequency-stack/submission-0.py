class FreqStack:

    def __init__(self):
        # Keep track of counts, and stack of stacks, each stack is the count frequency
        self.count = {}
        self.stacks = [[]] # Stack of stacks, the first is for count 1       

    def push(self, val: int) -> None:
        # Get the count of the value
        valCount = 1 + self.count.get(val, 0) # Default 0
        # Add this frequency to our hash map keeping track of counts for each value
        self.count[val] = valCount
        if valCount == len(self.stacks): # This means we need a new stack
            self.stacks.append([]) # This is for the new frequency
        # Add this to the corresponding count stack, it can't be the newest all the time.
        self.stacks[valCount].append(val)

    def pop(self) -> int:
        # Pop the top of the stacks of stacks, with the top stack's value
        poppedVal = self.stacks[-1].pop()

        # Update our structures before returning, reduce the count in our hashmap
        self.count[poppedVal] -= 1

        if not self.stacks[-1]: # We should remove this stack then as it's empty
            self.stacks.pop()
        
        return poppedVal
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()