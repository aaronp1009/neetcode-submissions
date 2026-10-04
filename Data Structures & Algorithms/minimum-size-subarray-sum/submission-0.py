class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float('inf')

        for r in range(len(nums)):
            total += nums[r]

            # This works because we are minimizing, so l will increase and minimize
            while total >= target:
                res = min(r-l+1, res)
                # Remove from our current total before we increment the left part of the window
                total -= nums[l]
                l += 1
        
        return 0 if res == float('inf') else res