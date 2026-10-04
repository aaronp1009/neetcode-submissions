class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l] # Swap left and right
                l, r = l + 1, r - 1 # Update the pointers
        
        n = len(nums)
        k = k % n # n-1 to be inbounds for indices of array

        # Reverse the whole array first
        reverse(0, n-1)
        # Reverse from start to k
        reverse(0, k-1) # Minus 1 to be the right index
        # Reverse from k to the end
        reverse(k, n-1)

        return