class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set for the nums
        setNums = set(nums)
        longest = 0

        for num in nums:
            length = 0
            # Check if this num could be a starting, num-1 can't be in the set
            if (num - 1) not in setNums:
                while (num + length) in setNums: # Find the longest consecutive sequence
                    length += 1
            
            longest = max(length, longest) # Overwrite the longest if with the max in between
    
        return longest
