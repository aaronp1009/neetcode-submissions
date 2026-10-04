class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Search range is from 1, to the max pile since we know the minimum hours is len(piles) <= h
        l, r = 1, max(piles)
        res = 0

        while l <= r:
            # Value we want to try, our mid point
            k = l + ((r-l) // 2)

            # Try this k, we need to loop through all piles to get the total time
            totalHours = 0
            for p in piles:
                totalHours += math.ceil(p / k) # Round up since we can't move onto the next pile in the same hour
            
            # Now update our search range appropriately depending on if totalHours exceeds our h,
            # we want to find the minimum k, so we need to continue searching a smaller range if it was successful
            if totalHours > h:
                # Took too much time, that means our k should be higher
                l = k + 1
            elif totalHours <= h:
                # Was able to complete it in time, BUT can we do better? Reduce our greater range
                r = k - 1
                # Store the result for an easy return
                res = k
            
        # Our k to return
        return res
