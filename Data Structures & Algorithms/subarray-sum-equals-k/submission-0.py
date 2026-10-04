class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSum = { 0 : 1} # Key is PrefixSum, Value is Count

        for n in nums:
            curSum += n
            # Check this curSum - k to get diff
            diff = curSum - k

            # If the diff is in the prefixSum hashmap, add the counts to the result
            res += prefixSum.get(diff, 0)

            # Add to the prefixSum for this current sum, if it already is there, increase the count
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

        return res