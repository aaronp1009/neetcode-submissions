class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # First make every number negative to simulate a maxHeap
        for i in range(len(nums)):
            nums[i] = -1 * nums[i]
        
        # Now let's make our maxHeap
        heapq.heapify(nums) # O(n)

        # Now pop k times to get kth largest, then invert the sign
        while k > 1:
            heapq.heappop(nums)
            k -= 1
        
        # Now our result should be the top
        res = heapq.heappop(nums)
        return -1 * res
