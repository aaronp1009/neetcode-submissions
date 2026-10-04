class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # Get prefix (values multiplied up until nums[i])
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix # First put in result array, this stores our prefixes
            prefix *= nums[i] # Update our prefix
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix # Multiply prefix * postfix, do not overwrite
            postfix *= nums[i]
        
        return res