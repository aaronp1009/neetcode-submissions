class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Create pointers for indices
        l, r = 0, len(heights)-1

        maxA = 0

        while l < r:
            # Take the min height, multiply by distance between
            # l and r
            minHeight = min(heights[l], heights[r])
            maxA = max(maxA, (r-l) * minHeight)

            # Update our pointers
            # only update the side we know will have a greater height
            # The intuition is that as the gap closes, if our current height is
            # larger, it will not be large.
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return maxA