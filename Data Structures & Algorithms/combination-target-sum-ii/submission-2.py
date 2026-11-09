class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() # Keep it sorted for dups

        def dfs(i, cur, total):
            if target == total:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return # Nothing
            
            cur.append(candidates[i]) # Branch for candidates[i]
            dfs(i+1, cur, total + candidates[i]) # Always + 1
            cur.pop() # Remove for the branch without candidates[i]

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(i+1, cur, total) # This is without since we incremented i to be unique after sorting
        
        dfs(0, [], 0) # Call our dfs/backtracking function
        return res