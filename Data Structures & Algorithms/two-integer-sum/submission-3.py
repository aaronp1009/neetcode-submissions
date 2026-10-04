class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Hashmap where value : index
        hashMap = {}

        for i, num in enumerate(nums):
            complement = target - num

            # Check if complement exists in map before adding current num
            if complement in hashMap:
                return [hashMap[complement], i]
            
            # Now we add our current num to the hashmap, value : index
            hashMap[num] = i