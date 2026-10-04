class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Define range for binary search, minimum weight capacity of the ship
        l, r = max(weights), sum(weights) # This is an O(n) operation
        res = r

        # Check the possible weights
        while l <= r:
            # Find the weight capacity to try
            capacity = l + ((r-l) // 2)

            totalDays = 1
            tempCapacity = capacity

            for w in weights:
                if tempCapacity >= w:
                    tempCapacity -= w
                else:
                    totalDays += 1
                    tempCapacity = capacity - w
            
            # Check valid ranges
            if totalDays <= days:
                # Check to see if we have a better result
                res = capacity
                r = capacity - 1
            else:
                # totalDays
                l = capacity + 1
        
        return res


