class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longest = 0

        for num in nums:
            length = 1
            # If no left neighbor in the set, num-1
            if (num-1) not in setNums:
                # Iterate and check how long this sequence could be
                while (num + length) in setNums:
                    length += 1 # This num must be a consecutive sequence
            longest = max(length, longest) # Take the maximum between the two
        
        return longest