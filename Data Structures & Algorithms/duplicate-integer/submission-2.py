class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()

        for i in range(len(nums)):
            if nums[i] in unique:
                return True
            unique.add(nums[i])

        return False