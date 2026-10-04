class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [] # We will only store the indices
        maxArea = 0

        # Loop one extra for the cleanup, this will pop everything in our stack
        for i in range(n+1):
            # While there are elements in stack, calculate the areas.
            # i == n is intentionally before for short-circuit evaluation
            while stack and (i == n or heights[stack[-1]] > heights[i]):
                # Get the height and width
                height = heights[stack.pop()] # Pop the value for real now
                width = i if not stack else i - stack[-1] - 1 # If no stack, we calculate the true distance
                # Update our maxArea if needed
                maxArea = max(maxArea, height * width)
            stack.append(i) # push current index, for the final loop, this just adds i == n so it doesn't matter.
        
        return maxArea