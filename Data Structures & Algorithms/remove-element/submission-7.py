class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for num in nums:
            # if you reach a num where num == val
            if num != val:
                nums[k] = num
                k += 1
                
        return k
            