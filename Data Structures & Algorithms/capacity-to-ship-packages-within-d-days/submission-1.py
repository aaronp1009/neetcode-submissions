class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # The minimum possible capacity must fit the heaviest package.
        # The maximum possible capacity is the total weight of all packages,
        # which would allow us to ship everything in one day.
        l, r = max(weights), sum(weights)
        res = r

        # Binary search for the minimum capacity that can ship
        # all packages within the given number of days.
        while l <= r:
            # Try the middle capacity.
            capacity = l + ((r - l) // 2)

            # Start with the first day.
            totalDays = 1
            tempCapacity = capacity

            # Simulate loading the packages in the required order.
            for w in weights:
                if tempCapacity >= w:
                    # Package fits on the current day.
                    tempCapacity -= w
                else:
                    # Package does not fit, so start a new day
                    # and load this package onto the new day.
                    totalDays += 1
                    tempCapacity = capacity - w # account for the current package

            # If this capacity can ship everything within the required days,
            # try a smaller capacity.
            if totalDays <= days:
                res = capacity
                r = capacity - 1
            else:
                # Capacity is too small, so try a larger capacity.
                l = capacity + 1

        return res


