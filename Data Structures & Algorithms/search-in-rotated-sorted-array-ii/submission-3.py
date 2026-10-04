class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Set up the pointers
        l, r = 0, len(nums)-1

        while l <= r: # We need to check cases like [1]
            m = l + ((r - l) // 2) # Get middle

            # Check if this middle is our target
            if nums[m] == target:
                return True
            
            # Since we can't determine which half is sorted (duplicates at boundaries)
            # just shrink the window by 1 on each side
            elif nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1

            # Right half [m..r] is sorted
            elif nums[m] <= nums[r]:
                # Check if target is in between here
                if nums[m] < target <= nums[r]:
                    # We want to search the right
                    l = m + 1
                else: # We want to search the left
                    r = m - 1
            
            # Left half [l..m] is sorted
            else:
                if nums[l] <= target < nums[m]:
                    # We want to search the left
                    r = m - 1
                else: # We want to search the right
                    l = m + 1

        # Didn't find anything, return False
        return False