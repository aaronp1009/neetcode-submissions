class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] # Array we will pass in to heapify (minHeap)

        for x, y in points:
            # Calculate dist
            dist = (x ** 2) + (y ** 2)
            # Add to our minHeap
            minHeap.append([dist, x, y])

        # Now heapify the list
        heapq.heapify(minHeap)

        # Go through and pop the k min elements
        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(minHeap) # We don't need dist in our result
            res.append([x, y])
        
        # Return this list
        return res