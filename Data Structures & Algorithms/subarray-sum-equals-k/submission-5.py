class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 # Holds the total number of subarrays
        curSum = 0 # We will add to this, then store it in our prefixSum hashmap
        prefixSum = { 0 : 1} # A subarray of 0 sum always exists, handles base cases

        for n in nums:
            # Increment our curSum
            curSum += n

            # Find the difference of curSum - k, this diff will be checked in prefixSum hashmap
            diff = curSum - k

            # If there is a count for that prefixSum,
            # add it to our result, this is a subarray that equals the sum
            res += prefixSum.get(diff, 0)

            # Add our curSum into the hashmap, do not override the current count
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

        return res
        