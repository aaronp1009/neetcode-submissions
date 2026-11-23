class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python does not have maxHeap, put negatives in minHeap
        stones = [-s for s in stones] # Make it all negative
        heapq.heapify(stones) # Create the minHeap

        while len(stones) > 1:
            first = heapq.heappop(stones) # First largest
            second = heapq.heappop(stones) # second largest

            # If they are equal, do nothing
            
            # If one is larger, pop the other, do the inverse since it is negative
            if second > first: # Example is -7 > -8
                heapq.heappush(stones, first - second) # Get the difference, would be -1 in our example
        
        stones.append(0) # Add one in just in case
        return abs(stones[0])