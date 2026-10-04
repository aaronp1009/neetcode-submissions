class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Minimum would be the max of the weights, max is the sum since we can just fit EVERYTHING
        # into one shipment at a time
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            # Get the middle capacity
            capacity = l + ((r-l) // 2)

            # Calculate the days for loading this shipment
            totalDays = 1
            tempCapacity = capacity

            # Go through the shipment weights
            for w in weights:
                # We can load onto our ship
                if tempCapacity >= w:
                    tempCapacity -= w
                else:
                    # We cannot load this onto the ship on this day
                    totalDays += 1
                    tempCapacity = capacity - w # Account for the current weight
                
            if totalDays <= days:
                # We will try better capacities
                r = capacity - 1
                res = capacity
            else:
                # We need to try a larger capacity, could not do it in time
                l = capacity + 1
        
        # Result stores our answer
        return res
