class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # Keep indices here
        maxArea = 0

        n = len(heights)

        for i in range(n + 1): # Plus 1 to do the final loop to pop all from the stack.
            start = i
            # i == n for the cleanup
            while stack and ((i == n) or heights[stack[-1]] > heights[i]):
                # Calculate the area, get the height and width
                height = heights[stack.pop()] # We only viewed the top in the loop
                width = i if not stack else i - stack[-1] - 1 # If our stack is empty, this calculates the distance between
                maxArea = max(maxArea, height*width) # Update our max is necessary
            stack.append(i) # Add our index to the stack
        
        return maxArea


