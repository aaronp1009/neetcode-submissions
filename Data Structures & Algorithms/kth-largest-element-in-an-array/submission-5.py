class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maxHeap solution, but using minHeap instead to avoid O(n) negative reassignment
        heapq.heapify(nums)

        while (len(nums) > k):
            heapq.heappop(nums) # Keep poppping until we have k left since it's minheap.
        
        # Our answer is at 0 because this is the kth largest, also the minimal out of the remaining k elements
        return nums[0]