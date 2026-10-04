class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Set up our left and right pointers
        l, r = 0, len(nums)-1

        while l <= r:
            # compute mid
            mid = l + ((r - l) // 2)

            # Check if we found our target
            if nums[mid] == target:
                return True
            
            # Check if our boundaries are duplicate, if so, just shrink each side
            elif nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            
            # The case for the right sorted portion [mid..r]
            elif nums[mid] <= nums[r]:
                # Check if our target is within middle to right
                if nums[mid] < target <= nums[r]:
                    # Our window is the the right side
                    l = mid + 1
                else: # Our window should be the left side
                    r = mid - 1
            
            # The case for the left sorted portin [l..mid]
            else:
                # Check if our target is within the left to middle
                if nums[l] <= target < nums[mid]:
                    # We want to search the left, update our right pointer
                    r = mid - 1
                else: # We want to search the right side, update our left pointer
                    l = mid + 1
            
        # We didn't find our answer
        return False