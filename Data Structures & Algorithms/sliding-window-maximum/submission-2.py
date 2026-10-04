class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() # Stores the index for window calculation
        l = r = 0

        while r < len(nums):
            # while the current is larger than the right of the queue, we want to pop since it's
            # going to a monotonically decreasing queue
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            
            # Now we are safe to add this value to the queue since we know it doesn't "increase"
            q.append(r)

            # Validate our queue contains elements of our window so far
            if l > q[0]:
                q.popleft()

            # Validate r is big enough for a window since we start at r = 0
            if (r + 1) >= k:
                # Max is the leftmost of queue, take index for the number
                output.append(nums[q[0]])
                # increment the left now, we will do the cleanup next loop
                l += 1
            
            # Always increase right
            r += 1
        return output