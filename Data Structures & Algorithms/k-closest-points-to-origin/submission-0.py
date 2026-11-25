class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] # This will be the list we convert to a heap
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        # Now take our list and convert to minHeap, using first key by default O(n)
        heapq.heapify(minHeap)

        # Now pop k elements for closest
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            # We only care about x and y
            res.append([x, y])
            k -= 1
        
        return res