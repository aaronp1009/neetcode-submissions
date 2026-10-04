class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # value : index

        for i, num in enumerate(nums):
            complement = target - num

            # if it's in there, check first before adding our new num
            if complement in hashMap:
                # We found a complement to this number that equals our target
                return [hashMap[complement], i]
            
            hashMap[num] = i # Now we are safe to add the num to our hashMap with index value


            