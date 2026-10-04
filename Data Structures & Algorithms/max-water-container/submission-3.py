class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Create pointers for our indices
        l, r = 0, len(heights)-1
        maxA = 0

        while l < r:
            # Our area is capped by the minimum height
            minHeight = min(heights[l], heights[r])
            # Take the max between our current max and newly computed area
            maxA = max(maxA, (r-l) * minHeight)

            # Update our pointers, only update the side that is smaller
            # if equal, doesn't matter which side
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxA