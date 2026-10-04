class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Set the left and right pointers
        l, r = 0, len(nums)-1

        while l < r:
            # Possible minimum, our current middle
            m = l + ((r - l) // 2)

            # If the middle < right, the minimum is in the left half (including m)
            if nums[m] < nums[r]:
                # Search to the left since right is larger that middle
                r = m
            # Otherwise the minimum is in the right half (after m)
            else:
                # This is for nums[m] >= nums[r], so we know the minimum is in the right half 
                l = m + 1
        
        # This pointer contains our minimum
        return nums[l]
