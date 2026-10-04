class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Have a left pointer
        l = 1

        # Iterator is our right pointer, start at index 1 to compare previous index
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]: # If there is a mismatch, we can update left pointer
                nums[l] = nums[r]
                l += 1
            # If there is a duplicate, the left pointer doesn't move.

        # Return k, where k == l pointer because that's how many elements are unique.
        return l


