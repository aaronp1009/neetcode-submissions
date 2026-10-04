class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Our solution set is the minimum subarray sum. This means
        # the max(nums) is our smallest minimum subarray sum and for simplicity, the sum(nums)
        # would be our largest minimum subarray sum.
        l, r = max(nums), sum(nums)
        res = r # Set it to our largest, we will be minimizing this anyway

        # Do a binary search to see if we can find a smaller minimum subarray sum
        # result will have our answer
        while l <= r:
            # A possible minimum subarray sum
            m = l + ((r - l) // 2)

            # We must split our nums array where each subarray is at most m size
            # and we will also keep track of the number of subarrays to compare with k
            subArrays = 1
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > m:
                    # We cannot fit into the current subarray, make a new one and start from there
                    subArrays += 1
                    curSum = n # This new n goes into the new subarray
            
            # Compare our subarray counts now, if we could split within k, keep searching for a better
            # answer (searching left), else, our m is too small, so we need to search right
            if subArrays <= k:
                # Store our result, the m we have is our possible minimum subarray sum
                res = m
                r = m - 1
            else:
                # Our possible minimum subarray sum was too small, search the right
                l = m + 1
        
        # Our result holds the answer
        return res

