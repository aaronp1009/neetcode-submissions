class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # Invert to simulate maxHeap
        heapq.heapify(stones)

        while len(stones) > 1: # Keep going
            first = abs(heapq.heappop(stones)) # largest
            second = abs(heapq.heappop(stones)) # second largest

            # If equal, both are destroyed, if not the difference is in the heap
            if first > second:
                heapq.heappush(stones, second - first) # Already adding it negative
            
        # only return if something is in
        return abs(stones[0]) if stones else 0