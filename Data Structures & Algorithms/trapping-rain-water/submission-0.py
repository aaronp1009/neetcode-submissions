class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case
        if not height:
            return 0
        
        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]

        totalWater = 0

        while l < r:
            # This is the minimum of the left and the right
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l]) # We do this first to not get negatives
                # Calculate the actual water from that max
                totalWater += leftMax - height[l]
            else: # If the rightMax is less than (or equal) to leftMax
                r -= 1
                rightMax = max(rightMax, height[r])
                # Calculate the actual water from that max
                totalWater += rightMax - height[r]

        return totalWater