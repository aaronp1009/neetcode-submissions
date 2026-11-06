class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = res | n
        
        return res * (2**(len(nums)-1)) # Combinatorics, each position is 2^n-1