class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy()) # Append copy to our result
                return
            if i >= len(nums) or total > target:
                return # Do nothing
            
            # Search with
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            # Search without
            curr.pop()
            dfs(i+1, curr, total)

        dfs(0, [], 0)
        return res # Stored in res
            