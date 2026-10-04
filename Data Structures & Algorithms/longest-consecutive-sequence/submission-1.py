class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set of the nums
        setNums = set(nums)

        # Initialize longest variable
        longest = 0

        for num in nums:
            length = 1 # Each number iterated makes the consecutive sequence start at 1
            if (num-1) not in setNums: # Check if it is a starting number (no left neighbor)
                while (num + length) in setNums: # Loops for consecutive numbers, increments length
                    length += 1
            longest = max(longest, length) # Only override max longest when length is greater
        
        return longest