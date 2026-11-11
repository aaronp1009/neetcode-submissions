class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # Allows us to skip values to avoid duplicates

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy()) # at end of array, copy into res
                return
            
            # with
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop() # Restore without for next step

            # without

            # Skip the dups
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, subset)
        

        backtrack(0, [])
        return res