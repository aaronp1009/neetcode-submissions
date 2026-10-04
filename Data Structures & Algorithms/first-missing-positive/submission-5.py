class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # First convert all negative values to a 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
    
        # Next, since we know negatives do not exist, we can mark them to become our "Hashset"
        # where the index is i - 1. It must be i-1 because the first missing positive can at
        # least be 1 but our array index starts at 0. Each index will map to the positive value (+1 of course)
        for i in range(len(nums)):
            val = abs(nums[i]) # Take absolute value in case we already marked this index
            if 1 <= val <= len(nums): # Value falls in our possible solution set
                if nums[val-1] > 0: # This is our first time seeing the value, hence why it is positive, let's mark it
                    nums[val-1] *= -1
                elif nums[val-1] == 0: # Edge case, can't really mark it so make it some number not in solution set
                    nums[val-1] = -1 * (len(nums) + 1)

        # Last loop to go through our input array, if the value at the index is not negative, it means we never found it
        # Start at 1 and go to the length of the array, just an off by one adjustment
        for i in range(1, len(nums)+1):
            if nums[i-1] >= 0:
                return i
        
        # If none of that occurred, worse case is len(nums)
        return len(nums)+1