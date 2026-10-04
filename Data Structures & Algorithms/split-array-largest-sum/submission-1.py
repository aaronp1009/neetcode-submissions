class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            m = l + ((r - l) // 2)

            subArrays = 1
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > m:
                    subArrays += 1
                    if subArrays > k: # We exceeded the subarray count
                        break
                    # new subarray has the curSum with the current n
                    curSum = n

            # Comparison for Binary Search
            if subArrays <= k:
                # Try to find a better solution
                r = m - 1
                res = m
            else:
                # Need to increase m
                l = m + 1
        
        # Return result
        return res