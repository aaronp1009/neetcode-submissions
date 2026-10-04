class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Keep track of the boundaries
        i, b1, b2 = 0, 0, len(nums)-1

        while i <= b2:
            if nums[i] == 0: # Set the boundary
                temp = nums[i]
                nums[i] = nums[b1]
                nums[b1] = temp
                b1 += 1
            elif nums[i] == 2:
                temp = nums[b2]
                nums[b2] = nums[i]
                nums[i] = temp
                b2 -= 1
                i -= 1

            i += 1

        return

