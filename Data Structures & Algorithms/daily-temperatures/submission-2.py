class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Store the index in the stack
        stack = [] # We only need the index for calculation, comparison can go into original array
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # Stack must exist to index into it
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # If our temp is larger than our top value in stack, get the distance in between
                smallIndex = stack.pop()
                res[smallIndex] = i - smallIndex # This will get the days gap in between
            # For the first iteration, and for temperatures[i] <= the top of the stack, we append the index
            stack.append(i)
        # Our result array is now updated
        return res
