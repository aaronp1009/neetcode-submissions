class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            # Get middle
            m = l + ((r-l) // 2) # Avoid integer overflow

            if nums[m] == target:
                return m
            elif nums[m] > target:
                # Update right pointer
                r = m - 1
            else:
                # Update left pointer
                l = m + 1
        
        # We didn't find anything
        return -1