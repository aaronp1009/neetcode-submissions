class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() # Stores the indices
        l = r = 0

        while r < len(nums):
            # While the queue exists and the current is greater than the right of queue, keep popping from right
            # We want a monotonically decreasing deque
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            
            # Now we are safe to add this index to our deque
            q.append(r)

            # Check if the deque is up to date with our window, if l is greater than q[0] (leftmost)
            # pop the leftmost
            if l > q[0]:
                q.popleft()
            
            # Check that the window is our k to append the max for this window
            if (r + 1) >= k: # Need to check this since r starts at 0 so we only want to start once greater than k
                output.append(nums[q[0]])
                # We can now shift our left
                l += 1
            
            r += 1
        
        return output



            
