class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set of the nums list for O(1) lookup
        setNums = set(nums)
        longest = 0

        for num in nums:
            length = 1 # Has to be one since it's the first num
            # You know num is a starting num when it is not in the set (no left value)
            if (num - 1) not in setNums:
                while (num + length) in setNums:
                    length += 1 # Increment length
            longest = max(longest, length) # If the length overwrites our longest, take it
        
        return longest