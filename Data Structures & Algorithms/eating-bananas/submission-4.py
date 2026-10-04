class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We know our solution range for k is [1, max(pile)] because the minimum total hours
        # will be len(p) <= h.
        l, r = math.ceil(sum(piles) / h), max(piles) # This is an O(n) operation
        res = r # Doesn't really matter, but we will set to the max(piles) amount because we know it will work

        while l <= r:
            # Calculate our k to try, binary search
            k = l + ((r-l) // 2) # Good practice for all languages

            # Use this k to see if we can eat within our time limit
            totalHours = 0
            for p in piles:
                # This will round up since we can't move to the next pile in the same hour
                totalHours += math.ceil(p / k)

            # Compare the total hours with our current time limit
            if totalHours <= h:
                # We could do everything in the time limit, but can we do better? Still need to try.
                # Store the result for an easy return. Reduce our right pointer to see if we can do better.
                r = k - 1
                res = k
            else:
                # This is where totalHours > h, we need to increase k
                l = k + 1
        
        # When the loop finishes, whatever is in result is our answer
        return res
            