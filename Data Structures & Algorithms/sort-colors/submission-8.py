class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Keep track of the boundaries
        i, b1, b2 = 0, 0, len(nums)-1

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= b2:
            if nums[i] == 0: # Set the boundary
                swap(b1, i)
                b1 += 1
            elif nums[i] == 2:
                swap(b2, i)
                b2 -= 1
                i -= 1

            i += 1

        return

