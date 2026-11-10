class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums, idx):
        if idx == len(nums):
            self.res.append(nums[:]) # Same as .copy()
            return
        # Go through each index, swap and then call backtrack
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, idx+1)
            nums[idx], nums[i] = nums[i], nums[idx] # Swap back to restore after recursion