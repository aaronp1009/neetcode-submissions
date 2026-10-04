class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Sanitize the array, mark any negatives our values not in the solution set to len(n)+1
        for i in range(n):
            if (nums[i] <= 0) or (nums[i] >= n+1):
                nums[i] = n + 1
        
        # Map the value of nums[i] to the indices of the input array, so i-1 to be in the same range
        # Mark seen values as negative, this is mimicking a Hashset
        for i in range(n):
            # Take the absolute value in case it was already marked as negative
            val = abs(nums[i])
            if 1 <= val <= n:
                # Take the absolute value first before setting to negative to avoid turning back to positive
                # adjust for off by one in input array, e.g. a value of 5 goes to nums[4]
                nums[val-1] = -abs(nums[val-1])
            
        # Find the positive index, make sure to add 1 for output/off by one adjustment
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # Worse case, the return is n + 1
        return n + 1


