class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left and right pointers
        l, r = 0, len(nums)-1

        while l <= r: # also checks for single length nums
            mid = l +((r-l) // 2) # Get the middle

            if target == nums[mid]:
                return mid # We found our index
            elif nums[l] <= nums[mid]: 
                # If target is less than left boundary, but greater than mid
                if target < nums[l] or target > nums[mid]:
                    # Target is NOT in between, so left is updated
                    l = mid + 1
                else:
                    # Target is in between, update the right pointer
                    r = mid - 1
            else:
                # Right portion
                # If target is greater than our right boundary and less than middle
                # we are not in the right portion
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    # Target is in between, update the left pointer
                    l = mid + 1
            
        # Loop ended, we didn't find anything, return -1
        return -1