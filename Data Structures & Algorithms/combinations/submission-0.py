class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [] # Store our results

        def dfs(start, comb): # Start is a number, comb is a list of the current combination
            if len(comb) == k: # Nothing else to add to this combination
                res.append(comb.copy()) # Take a copy so the comb in our result doesn't get modified
                return

            # Loop through to recursively add to our combination
            for i in range(start, n+1): # N+1 since last is not inclusive in python
                comb.append(i)
                dfs(i+1, comb) # Start at everything i+1
                comb.pop()
            
        dfs(1, []) # problem says [1, n]
        return res