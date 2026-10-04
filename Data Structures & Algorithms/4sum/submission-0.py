class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort nums
        nums.sort()
        res = []
        curKList = []

        def kSum(k, start, target1):
            # Two Sum II solution
            if k == 2:
                l, r = start, len(nums)-1

                while l < r:
                    curSum = nums[l] + nums[r]

                    # Adjust the pointers based on if current sum is too big or little
                    if curSum < target1:
                        l += 1
                    elif curSum > target1:
                        r -= 1
                    else:
                        # Append the current K list plus the last two to our results
                        res.append(curKList + [nums[l], nums[r]])
                        l += 1
                        r -= 1

                        # Check duplicates, only need to check one, but could check both too.
                        # I will check both
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                return

            # Other case, calling KSum recursively
            for i in range(start, len(nums) - k + 1): # minus k so we have a list with enough elements
                # Skip duplicates for the first
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                curKList.append(nums[i])
                kSum(k-1, i+1, target1-nums[i])
                curKList.pop() # Clears the current list for the next one after kSum returns
            return

        kSum(4, 0, target)
        return res
