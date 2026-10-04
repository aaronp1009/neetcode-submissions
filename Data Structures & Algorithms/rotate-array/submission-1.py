class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Make k fit within length of nums
        n = len(nums)
        k = k % n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l] # Swap l and r
                l, r = l + 1, r - 1 # Update pointers after swap
            
        # First reverse the whole array
        reverse(0, n-1)
        # Then reverse from start to k (k-1 to stay in bounds)
        reverse(0, k-1)
        # Now reverse everything after k to the end
        reverse(k, n-1)

        return