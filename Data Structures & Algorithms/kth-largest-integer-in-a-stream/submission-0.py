class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        # Make sure only k elements in heap
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) # Pop from minHeap

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # Put this val in our heap
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # Return the kth larget
        return self.minHeap[0]
        
