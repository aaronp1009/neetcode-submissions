class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Set the left and right pointers
        l, r = 0, len(nums)-1

        while l < r:
            # Possible minimum, our current middle
            m = l + ((r - l) // 2)

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        # This pointer contains our minimum
        return nums[l]
