class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Have a left and right pointer
        l, r = 0, len(nums)-1

        while l <= r:
            # Get middle, avoid integer overflow (other languages)
            m = l + ((r-l) // 2)

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1 # middle is too big, this is our new right boundary
            else:
                l = m + 1 # middle is too small, this is our new left boundary
        return -1 # Didn't find anything