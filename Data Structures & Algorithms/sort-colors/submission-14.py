class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Define pointers
        i, l, r = 0, 0, len(nums) - 1

        def swap(i, j):
            # Store the first in temp
            tmp = nums[i]

            # Swap j and i values
            nums[i] = nums[j]

            # Take our "lost" temp and put back in j 
            nums[j] = tmp

        while i <= r:
            if nums[i] == 0:
                # Swap the left and current, increment left ptr
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                # Swap the right and current, decrement right ptr
                # Cancel incrementing i to avoid introducing 0s into the middle
                swap(r, i)
                r -= 1
                i -= 1
            i += 1 # To make the current iterator ptr reach the right ptr

        return
