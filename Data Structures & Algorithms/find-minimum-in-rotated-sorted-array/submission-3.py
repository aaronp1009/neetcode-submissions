class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Create our left and right pointers
        l, r = 0, len(nums)-1

        while l < r: # Not equal since this will save an iteration and l will contain minimum
            m = l + ((r - l) // 2)

            # If the middle < right, that means our answer is towards the left, including the middle 
            if nums[m] < nums[r]:
                r = m
            else:
                # This implies middle >= right, in that case, our answer is towards the right,
                # so update left
                l = m + 1
        
        # When loop finishes, left has the answer
        return nums[l]