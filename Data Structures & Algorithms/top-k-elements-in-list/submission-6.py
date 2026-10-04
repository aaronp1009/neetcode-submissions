class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hashmap for the counts
        count = {}

        # List of lists, each index represents the count,
        # going in reverse order k times will get you the k most frequent
        # values
        freq = [[] for i in range(len(nums))] # k is at most, size of nums

        for num in nums:
            count[num] = 1 + count.get(num, 0) # If it is in there, increment return 0 if not
        
        # Go through counts, add to correct index in freq
        for num, freq_index in count.items():
            freq[freq_index-1].append(num) # Add to the freq array, index represents freq of that num
        
        res = []
        start = 0
        for i in range(len(freq)-1, -1, -1):
            # If the frequency bucket is not empty
            if freq[i]:
                if k == start:
                    return res # If our start equals our k, we have enough top K frequent
                # If not, add to our result
                for num in freq[i]:
                    res.append(num) # Add this value to our result array
                    start += 1
            else:
                continue

        return res

        

