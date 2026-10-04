class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)] # We don't use 0 index

        # Create the count hashmap, number maps to frequency
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Use the indices of freq to map frequency index to values
        for n, c in count.items():
            freq[c].append(n) # Add the number to that count index
        
        res = []
        for i in range(len(nums), 0, -1): # Iterate backwards to index 0
            for n in freq[i]:
                res.append(n) # Since we're going backwards, append to our res
                if len(res) ==  k:
                    return res