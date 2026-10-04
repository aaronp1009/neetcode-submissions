class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search is splitting the area in halves to find the answer
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2 # Get the middle

            # Check if value is greater or less than middle, this will update our l, r pointers
            if nums[m] > target:
                # We are in the lower half, update right pointer
                r = m - 1
            elif nums[m] < target:
                # We are in the upper half, left is the middle now.
                l = m + 1
            else:
                # We found our answer
                return m
        
        return -1
