class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] # keeps tracks of all of our subsets
        subset = [] # We will be recursively populating this

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy()) # Append the clean copy
                return
            
            # Do the recursive call with nums[i] to include in subset
            subset.append(nums[i])
            dfs(i + 1) # To go to next one, we will start at 0

            # Do the recursive call without nums[i] to include in subset
            subset.pop() # We can just pop it so it's empty
            dfs(i + 1) # Recursive stack for this

            return subset
        
        dfs(0)
        return res # Res contains our lists