class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        equal_subset = total_sum // k
        subsets = [0] * k

        if total_sum / k != equal_subset: # That means there is a decimal, can't be divided
            return False
        
        # Sort reverse just to have the larger ones in the beginning to know
        nums.sort(reverse=True)

        def backtrack(i):
            if i == len(nums): # We got all our equal subsets
                return True
            
            seen = set()

            for j in range(k):
                check_subset = subsets[j] + nums[i]
                if check_subset <= equal_subset and check_subset not in seen:
                    # We can add this
                    subsets[j] += nums[i]
                    if backtrack(i+1): # Check the remaining
                        return True
                    # Undo now, this is the backtracking
                    subsets[j] -= nums[i]
                    seen.add(check_subset)
            # We never found a solution, return False
            return False
        
        return backtrack(0)