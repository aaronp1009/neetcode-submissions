class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonically (decreasing or equal) stack
        stack = [] # Store tuple, (temp, index)
        res = [0] * len(temperatures) # 0 is our default for this

        for i, t in enumerate(temperatures): # This lets us get the index as well for calculating days between
            # First time will not have stack, we must check to compare the top
            while stack and t > stack[-1][0]: # Since we want to store (temp, index), we must get the temp
                stackTemp, stackIndex = stack.pop() # We found a temp larger, so let's pop and calculate days between
                # Take our current i (larger) subtract the index in the stack for days between
                res[stackIndex] = i - stackIndex
            # This is for the first time, and also will add t <= to our stack
            stack.append((t, i)) # Make sure to add a tuple to the stack
        
        # Result holds the array with the calculations
        return res