class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # The minimum capacity is the max weight, max is fitting all weights
        # into one ship
        l, r = max(weights), sum(weights)
        res = r # Set result to our maximum possible capacity, this will be minimized

        while l <= r:
            cap = l + ((r - l) // 2)

            # Calculate how many days to fit into this cap
            curSum = 0
            daysUsed = 1

            for w in weights:
                if curSum + w > cap:
                    daysUsed += 1 # We need a new day if the weight is larger than our cap
                    curSum = w # Start with this new weight on our new day in our boat
                else:
                    curSum += w
            
            # Now binary search based on this
            if daysUsed <= days:
                # See if there is a better result, but save our current
                r = cap - 1
                res = cap
            else:
                # Did not fit in the number of days, need to increase our capacity range
                l = cap + 1

        # Result is in res
        return res
