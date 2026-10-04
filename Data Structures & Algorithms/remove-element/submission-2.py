class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        # Go through every element
        for num in nums:
            # if the current number in nums is not equal to value,
            # we can safely replace starting from the beginning of the array
            if num != val:
                nums[k] = num
                k += 1
        return k
