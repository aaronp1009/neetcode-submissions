class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search is splitting the area in halves to find the answer
        l, r = 0, len(nums)

        while l < r:
            m = (l + (r-1)) // 2 # Get the middle

            # Check if value is greater or less than middle, this will update our l, r pointers
            if target < nums[m]:
                # We are in the lower half, update right pointer
                r = m
            elif target >= nums[m]:
                # We are in the upper half, left is the middle now. This is the lower bound solution
                # so we must check after all iterations since target may equal nums[m]
                l = m + 1
        
        return l - 1 if (nums[l-1] == target) else -1
