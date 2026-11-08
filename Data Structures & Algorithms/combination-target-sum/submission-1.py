class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return
            elif i >= len(nums) or total > target:
                return # Do nothing
            
            cur.append(nums[i]) # Add to our cur
            dfs(i, total + nums[i]) # This is the backtracking with the value
            cur.pop() # Remove for backtracking without
            dfs(i+1, total) # No need to add nums[i] since without

        # Call our dfs function now
        dfs(0, 0)
        return res