class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l <= r:
            mid = l + ((r-l) // 2) # Avoid int overflow
            midSquared = mid * mid

            if midSquared > x:
                # Mid is too large, reduce the right pointer
                r = mid - 1
            elif midSquared < x:
                # Mid is too small, increase the left pointer
                l = mid + 1
            else:
                return mid # We have an answer
        
        # If we didn't find anything, we need to return the lower, so maybe l-1?
        return l-1