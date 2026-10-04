class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # We must get the peak index, then binary search the left and binary search the right
        length = mountainArr.length()

        l, r = 0, length-1
        while l <= r:
            m = l + ((r - l) // 2)

            left, mid, right = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)

            # If we have the peak, then left <= mid >= right
            if left < mid < right:
                # Still ascending, not at the peak
                l = m + 1
            elif left > mid > right:
                # Still desecending
                r = m - 1
            else:
                # We found a peak
                break
        peak = m

        # Search left for target (ascending)
        l, r = 0, peak
        while l <= r:
            m = l + ((r - l) // 2)
            val = mountainArr.get(m)

            # Check value
            if val > target:
                # Reduce search range on right
                r = m - 1
            elif val < target:
                l = m + 1
            else:
                return m
        
        # Search right (descending)
        l, r = peak+1, length-1
        while l <= r:
            m = l + ((r - l) // 2)
            val = mountainArr.get(m)

            # Check value (flipped cases cause descending)
            if val < target:
                # Reduce search range on right
                r = m - 1
            elif val > target:
                l = m + 1
            else:
                return m

        # After searching left and right, target was not found
        return -1
