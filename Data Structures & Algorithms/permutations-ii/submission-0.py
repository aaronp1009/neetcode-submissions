class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = {n:0 for n in nums} # Create a hashmap with 0 for each
        # Make the counts accurate
        for n in nums:
            count[n] += 1
        
        # backtrack function
        def backtrack(perm):
            if len(perm) == len(nums): # We found a permutation
                res.append(perm.copy()) # Recursive stack might modify it
                return
            
            # Use hashmap for recursion to avoid dup permutations
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1 # Decrease count before calling our backtrack function
                    backtrack(perm)

                    # Cleanup to restore for next
                    perm.pop()
                    count[n] += 1
        
        # Call our backtrack from outside
        backtrack([])
        return res # Stores the result
