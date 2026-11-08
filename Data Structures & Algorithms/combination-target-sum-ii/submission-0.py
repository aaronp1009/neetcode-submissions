class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] # Store our result
        candidates.sort() # Sorting is O(nlogn)

        def dfs(idx, path, cur):
            if cur == target:
                res.append(path.copy()) # We found a solution, add to result
                return
            
            # Check from index to lenth of candidates
            for i in range(idx, len(candidates)):
                # If our i is larger than our starting index and our candidate is the same as the previous,
                # keep going
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if cur + candidates[i] > target:
                    break # No need to continue this loop
                
                # Add to our path
                path.append(candidates[i])
                dfs(i+1, path, cur + candidates[i])
                path.pop()

        
        # Call our helper from outside
        dfs(0, [], 0)
        return res
                