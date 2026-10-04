class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() # Sort our nums array
        res = [] # Track our results, we return this in the end
        curKList = [] # Our curKList for each recursion

        def kSum(k, start, target):
            # Base case for recursion
            if k == 2: # Two Sum II
                l, r = start, len(nums)-1

                while l < r:
                    # Get current sum
                    curSum = nums[l] + nums[r]

                    # Adjust left or right if current sum is too small/big
                    if curSum < target:
                        l += 1
                    elif curSum > target:
                        r -= 1
                    else: # We have a match for the last two of kSum
                        res.append(curKList + [nums[l], nums[r]])

                        # Increment/Decrement pointers
                        l += 1
                        r -= 1

                        # Handle duplicates, we only need to do one pointer, but lets take care of both
                        # for more efficiency
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                return

            # Recursive case
            for i in range(start, len(nums)-k+1): # Minus k since our array should contain that many for kSum
                # Handle duplicates for i
                if i > start and nums[i] == nums[i-1]:
                    continue

                # Add our nums[i] to curKList and make sure to adjust our target for kSum recursion
                curKList.append(nums[i])
                kSum(k-1,i+1,target-nums[i])
                curKList.pop() # Clear the curKList for the next one
            return
        # Call our helper kSum
        kSum(4, 0, target)
        return res