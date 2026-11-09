class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() # This is similar to 3sum, we have to use sorting for making sure no dups

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total >= target:
                return # Nothing to do here, not valid
            
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])
            cur.pop() # This is after the recursion

            # skip candidates[i], we have to go through the sorted
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res